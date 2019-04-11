# Copyright 2019 Kensho Technologies, LLC.
"""Module for Wikidata linked data interface endpoints."""
import logging

import requests
from qwikidata import typedefs

logger = logging.getLogger(__name__)
WIKIDATA_LDI_URL = "https://www.wikidata.org/wiki/Special:EntityData"
VALID_ENTITY_PREFIXES = ("Q", "P", "L")


class LdiResponseNotOk(Exception):
    pass


class InvalidEntityId(Exception):
    pass


def get_entity_dict_from_api(
    entity_id: typedefs.EntityId, base_url: str = WIKIDATA_LDI_URL
) -> typedefs.EntityDict:
    """Get a dictionary representing a wikidata entity from the linked data interface API.

    https://www.wikidata.org/wiki/Wikidata:Data_access#Linked_Data_interface

    Parameters
    ----------
    entity_id
      A Wikidata entity id beginning with "Q", "P", or "L" (e.g. "Q42")
    base_url
      The linked data interface URL to use

    Examples
    --------
    Get the entity dictionary for item Q42,

    ::

      >>> entity_dict = get_entity_dict_from_api('Q42')
      >>> pprint(entity_dict, indent=4, depth=1)
      {   'aliases': {...},
          'claims': {...},
          'descriptions': {...},
          'id': 'Q42',
          'labels': {...},
          'lastrevid': 716282445,
          'modified': '2018-07-27T08:03:25Z',
          'ns': 0,
          'pageid': 138,
          'sitelinks': {...},
          'title': 'Q42',
          'type': 'item'}}}

    """
    if not isinstance(entity_id, str):
        raise InvalidEntityId(
            'entity_id must be a string (e.g. "Q42") but got entity_id={}.'.format(entity_id)
        )
    if not entity_id[0] in VALID_ENTITY_PREFIXES:
        raise InvalidEntityId(
            "entity_id must start with one of {} but got entity_id={}.".format(
                VALID_ENTITY_PREFIXES, entity_id
            )
        )

    url = "{}/{}.json".format(base_url, entity_id)
    response = requests.get(url)
    if response.ok:
        entity_dict_full = response.json()
    else:
        raise LdiResponseNotOk(
            "input entity id: {}, "
            "response.headers: {}, "
            "response.status_code: {}, "
            "response.text: {}".format(
                entity_id, response.headers, response.status_code, response.text
            )
        )

    # remove redundant top level keys
    returned_entity_id = next(iter(entity_dict_full["entities"]))
    entity_dict = entity_dict_full["entities"][returned_entity_id]

    if entity_id != returned_entity_id:
        logger.warning(
            "Wikidata redirect detected.  Input entity id={}. Returned entity id={}.".format(
                entity_id, returned_entity_id
            )
        )

    return entity_dict
