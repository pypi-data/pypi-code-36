# -*- coding: utf-8 -*-
"""
TFS API python 3 version
"""
import os
import re
from copy import deepcopy

from requests.structures import CaseInsensitiveDict
from six import iteritems


class TFSObject(object):
    def __init__(self, data=None, tfs=None, uri='', underProject=None):
        """
        Base tfs recource object initialization

        :param data: raw content of the resource
        :param tfs: ``TFSAPI`` instance
        :type tfs: TFSAPI
        :param uri: uri of resource
        :type uri: str
        :param underProject: resource is under the project in the path
        """
        # TODO: CaseInsensitive Dict

        self.tfs = tfs
        self.uri = uri
        self._underProject = underProject
        self.data = data
        # list of resources from _links property to expose as attributes
        self._links_attrs = []

        self._data = self.data  # legacy, some people can use private method

    def __dir__(self):
        """
        Extend standart dir() with attribute in `_links`
        listed in self._links_attrs

        :return: extended list of attribute name
        """
        original = super(TFSObject, self).__dir__()

        if not self.data:
            return original

        extend = [x for x in self.data.get('_links', {}) if x in self._links_attrs]
        return original + extend

    def __get_object_by_links(self, name):
        """
        Dynamically add property for all ``_links`` field in JSON, if exist
        """
        links = self.data.get('_links', {})  # or emtpy if _links is not exist
        url = links[name]['href']
        return self.tfs.get_tfs_resource(url)

    def __getattr__(self, name):
        """
        If object have not attribute, try search in `_links` and return new TFSObject
        :param name:
        :return: mapped or unknown tfs object
        """
        if self.data and name in self.data.get('_links', {}):
            return self.__get_object_by_links(name)
        raise AttributeError("'{}' object has no attribute '{}'".format(self.__class__.__name__, name))

    # TODO: implement better repr
    # def __repr__(self):
    #     _repr = ''
    #     for k, v in self.data.items():
    #         _repr += to_str(k) + ' = ' + to_str(v) + '\n'
    #     return _repr

    def __getitem__(self, key):
        return self.data[key]

    def __setitem__(self, key, value):
        """
        We not implement default behavior, use class for it
        :param key:
        :param value:
        :return:
        """
        raise NotImplementedError

    def get(self, key, default=None):
        return self.data.get(key, default)


class UnknownTfsObject(TFSObject):
    """ Not yet known Resource from TFS. """

    def __init__(self, tfs, raw=None, uri='unknownResource', underProject=None):
        """

        :param tfs: instance of :class:`TFSAPI`
        :type tfs: TFSAPI
        :param raw: raw json content of the resource
        :type raw: str
        :param uri: uri of the recource
        :type uri: str
        :param underProject: indicates that resource located under the project path, None if location is unknown
        """
        # list of fields to exclude from resource translation and assign as a raw json value
        self.raw_attrs = ['_links']
        super().__init__(raw, tfs, uri=uri, underProject=underProject)
        if raw:
            self._parse_raw(raw)

    def _find(self, ids):
        """ Fills up the resource based on the resource's id.

        :param ids: ids to replace id placeholders in the uri
        :type ids: Union[Tuple[str, str], int, str]
        """
        uri = self.tfs.substitute_ids(self.uri, ids)
        self._load(uri)

    def _load(self, uri):
        """ Load a resource.

        :param uri: uri of the resource to get
        :type uri: str
        """
        result = self.tfs.get_json(uri, underProject=self._underProject)
        self._parse_raw(result)

    def _parse_raw(self, raw):
        """Parse a raw dictionary to create a resource.

        :type raw: Dict[str, Any]
        """
        self.data = raw
        if not raw:
            raise NotImplementedError("We cannot instantiate empty resources: %s" % raw)
        raw2resource(raw, self, self.tfs)


class Workitem(UnknownTfsObject):
    def __init__(self, tfs=None, raw=None):
        self.id = None
        self.fields = None
        # Use prefix in automatically lookup.
        # We don't need use wi['System.History'], we use simple wi['History']
        self._system_prefix = 'System.'

        super().__init__(tfs, raw, 'wit/workItems/{0}', underProject=False)
        self._links_attrs.extend(['workItemHistory', 'workItemRevisions', 'workItemType', 'workItemUpdates'])

    def _parse_raw(self, raw):
        self.raw_attrs.extend(['fields'])
        super()._parse_raw(raw)

        if not self.id:
            self.id = self.url.split('/')[-1]
        if self.fields:
            self.fields = CaseInsensitiveDict(self.fields)
            self._fields = self.fields

    def __setitem__(self, key, value):
        field_path = "/fields/{}".format(key)
        update_data = [dict(op="add", path=field_path, value=value)]
        raw = self.tfs.update_workitem(self.id, update_data)
        self.__init__(self.tfs, raw)

    def get(self, key, default=None):
        if key in self.fields:
            return self.fields[key]

        # try to automatically add prefix
        key = self._add_prefix(key)
        return self.fields.get(key, default)

    def __getitem__(self, key):
        if key in self.fields:
            return self.fields[key]

        # try to automatically add prefix
        key = self._add_prefix(key)
        return self.fields[key]

    def _add_prefix(self, key):
        if key.startswith(self._system_prefix):
            return key
        else:
            return self._system_prefix + key

    def _remove_prefix(self, key):
        if key.startswith(self._system_prefix):
            return key[len(self._system_prefix):]
        else:
            return key

    @property
    def field_names(self):
        return [self._remove_prefix(x) for x in self.fields]

    @property
    def history(self):
        return self.workItemHistory

    @property
    def revisions(self):
        return self.workItemRevisions

    def find_in_relation(self, relation_type):
        """
        Get relation by type\\name. Auto add

        :param relation_type:
        :return:
        """
        found = []
        for relation in self.data.get('relations', []):
            # Find as is, e.g. 'AttachedFile' or more smartly.
            # Found 'Hierarchy-Forward' in 'System.LinkTypes.Hierarchy-Forward'
            if relation_type == relation.get('rel', '') \
                    or relation.get('rel', '').endswith(relation_type):
                found.append(relation)
        return found

    def _find_in_relation(self, relation_type, return_one=True):
        """
        Find relation type in relations and return one or list
        one use for Parent WI
        """
        ids = []
        relations = self.find_in_relation(relation_type)
        for relation in relations:
            id_ = relation['url'].split('/')[-1]
            id_ = int(id_)
            ids.append(id_)
        if return_one:
            return ids[0] if ids else None
        else:
            return ids

    @property
    def parent_id(self):
        return self._find_in_relation('Hierarchy-Reverse', return_one=True)

    @property
    def parent(self):
        if self.parent_id is None:
            return None
        return self.tfs.get_workitem(self.parent_id)

    @property
    def child_ids(self):
        return self._find_in_relation('Hierarchy-Forward', return_one=False)

    @property
    def childs(self):
        if self.child_ids:
            return self.tfs.get_workitems(self.child_ids)
        else:
            return []

    @property
    def attachments(self):
        return [x for x in self.relations if isinstance(x, Attachment)]

    def add_relations_raw(self, relations_raw, params=None):
        """
        Add attachments, related (work item) links and/or hyperlinks

        :param relations_raw: List of relations. Each relation is a dict with the following keys: rel, url, attributes
        """
        # remove ID from attributes as it has to be unique
        copy_raw = [deepcopy(relation) for relation in relations_raw]
        for relation in copy_raw:
            if 'attributes' in relation:
                if 'id' in relation['attributes']:
                    del relation['attributes']['id']

        path = '/relations/-'
        update_data = [dict(op="add", path=path, value=relation) for relation in copy_raw]
        if update_data:
            raw = self.tfs.update_workitem(self.id, update_data, params)
            self.__init__(raw, self.tfs)


class Attachment(UnknownTfsObject):
    def __init__(self, tfs=None, raw=None):
        super().__init__(tfs, raw, 'wit/attachments/{0}', underProject=False)

    def _parse_raw(self, raw):
        super()._parse_raw(raw)

        self.id = self.url.split('/')[-1]  # Get UUID from url
        self.name = self.attributes.name

    def download(self, path='.'):
        path = os.path.join(path, self.name)
        self.tfs.download_file(self.url, path)


class Changeset(UnknownTfsObject):
    def __init__(self, tfs, raw=None):
        super().__init__(tfs, raw, uri="tfvc/changesets/{0}", underProject=False)

    def _parse_raw(self, raw):
        super()._parse_raw(raw)
        self.id = self.changesetId

    @property
    def workitems(self):
        wi_links = self.tfs.get_tfs_resource('tfvc/changesets/{}/workItems'.format(self.id),
                                             underProject=False)
        ids = [x.id for x in wi_links]
        workitems = self.tfs.get_workitems(ids)
        return workitems


class TFSQuery(UnknownTfsObject):
    def __init__(self, tfs=None, raw=None):
        super().__init__(tfs, raw, uri='wit/queries{0}?api-version=2.2', underProject=True)
        self._workitems = None

    def _parse_raw(self, raw):
        super()._parse_raw(raw)

        # run saved query using WIQL
        self.result = self.tfs.run_saved_query(self.id)
        self.columns = tuple(i['referenceName'] for i in self.result['columns'])
        self.column_names = tuple(i['name'] for i in self.result['columns'])

    @property
    def workitems(self):
        if not self._workitems:
            self._workitems = self.tfs.get_workitems((i['id'] for i in self.result['workItems']))
        return self._workitems


class Wiql(UnknownTfsObject):
    """
    Work Item Query Language
    """

    def __init__(self, tfs=None, raw=None):
        super().__init__(tfs, raw, 'wit/wiql/{0}?api-version=2.2', underProject=True)
        self.result = self.data

    @property
    def workitem_ids(self):
        ids = [x['id'] for x in self.data['workItems']]
        return ids

    @property
    def workitems(self):
        return self.tfs.get_workitems(self.workitem_ids)


class GitRepository(UnknownTfsObject):
    def __init__(self, tfs, raw=None):
        super().__init__(tfs, raw, "git/repositories/{0}", underProject=False)


class Project(UnknownTfsObject):
    def __init__(self, tfs, raw=None):
        super().__init__(tfs, raw, "projects/{0}", underProject=False)

    @property
    def teams(self):
        return self.tfs.teams(projectId=self.id)


class Team(UnknownTfsObject):
    def __init__(self, tfs, raw=None):
        super().__init__(tfs, raw, "projects/{0}/teams/{1}", underProject=False)


class Build(UnknownTfsObject):
    def __init__(self, tfs, raw=None):
        super().__init__(tfs, raw, "build/Builds/{0}", underProject=True)


class Definition(UnknownTfsObject):
    def __init__(self, tfs, raw=None):
        super().__init__(tfs, raw, "build/Definitions/{0}", underProject=True)


class Identity(UnknownTfsObject):
    def __init__(self, tfs, raw=None):
        super().__init__(tfs, raw, 'Identities/{0}', underProject=False)

#################################################################################
# Utilities
#################################################################################


def raw2resource(raw, top=None, tfs=None):
    """ Convert a raw valie into a TFTObject object.

    Recursively walks a dict structure, transforming the properties into attributes
    on a new ``TfsObject`` object of the appropriate type
    (if an ``url`` link is present and class found in the class map)
    or a ``TopLevelWrapper`` object.
    """
    if top is None:
        top = TopLevelWrapper(raw)

    seqs = tuple, list, set, frozenset
    for i, j in iteritems(raw):
        if isinstance(j, dict):
            if isinstance(top, UnknownTfsObject) and i in top.raw_attrs:
                setattr(top, i, j)
            elif 'url' in j:
                resource = class_for_resource(j['url'])(tfs, j)
                setattr(top, i, resource)
            else:
                setattr(
                    top, i, raw2resource(j, tfs=tfs))
        elif isinstance(j, seqs):
            seq_list = []
            for seq_elem in j:
                if isinstance(seq_elem, dict):
                    if 'url' in seq_elem:
                        resource = class_for_resource(seq_elem['url'])(
                            tfs, seq_elem)
                        seq_list.append(resource)
                    else:
                        seq_list.append(
                            raw2resource(seq_elem, tfs=tfs))
                else:
                    seq_list.append(seq_elem)
            setattr(top, i, seq_list)
        else:
            setattr(top, i, j)
    return top


resource_class_map = {
    r'wit/attachments/[^/]+$': Attachment,
    r'build/Builds/[^/]+$': Build,
    r'tfvc/changesets/[^/]+$': Changeset,
    r'build/Definitions/[^/]+$': Definition,
    r'git/repositories/[^/]+$': GitRepository,
    r'Identities/[^/]+$': Identity,
    r'projects/[^/]+$': Project,
    r'wit/queries/.+$': TFSQuery,
    r'projects/[^/]+/teams/[^/]+$': Team,
    r'wit/wiql/[^/]+': Wiql,
    r'wit/workItems/[^/]+$': Workitem
}


def class_for_resource(path):
    for resource in resource_class_map:
        if path and re.search(resource, path):
            return resource_class_map[resource]
    else:
        return UnknownTfsObject


class TopLevelWrapper(object):
    def __init__(self, raw):
        __bases__ = raw  # noqa
