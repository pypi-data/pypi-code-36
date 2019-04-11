# -*- coding: utf-8 -*-
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType
from pyangbind.lib.yangtypes import RestrictedClassType
from pyangbind.lib.yangtypes import TypedListType
from pyangbind.lib.yangtypes import YANGBool
from pyangbind.lib.yangtypes import YANGListType
from pyangbind.lib.yangtypes import YANGDynClass
from pyangbind.lib.yangtypes import ReferenceType
from pyangbind.lib.base import PybindBase
from collections import OrderedDict
from decimal import Decimal
from bitarray import bitarray
import six

# PY3 support of some PY2 keywords (needs improved)
if six.PY3:
  import builtins as __builtin__
  long = int
elif six.PY2:
  import __builtin__

class yc_ipAddress_vlan_ip_schema__VLAN_IP_ipAddress(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module vlan_ip_schema - based on the path /VLAN_IP/ipAddress. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_path_helper', '_extmethods', '__ipv4Address','__ipv6Address',)

  _yang_name = 'ipAddress'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    helper = kwargs.pop("path_helper", None)
    if helper is False:
      self._path_helper = False
    elif helper is not None and isinstance(helper, xpathhelper.YANGPathHelper):
      self._path_helper = helper
    elif hasattr(self, "_parent"):
      helper = getattr(self._parent, "_path_helper", False)
      self._path_helper = helper
    else:
      self._path_helper = False

    self._extmethods = False
    self.__ipv4Address = YANGDynClass(unique=True, base=TypedListType(allowed_type=RestrictedClassType(base_type=six.text_type, restriction_dict={u'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])/(([0-9])|([1-2][0-9])|(3[0-2]))'})), is_leaf=False, yang_name="ipv4Address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://north-api.aliababa.com/schema/vlan/', defining_module='vlan_ip_schema', yang_type='inet:ipv4-prefix', is_config=True)
    self.__ipv6Address = YANGDynClass(unique=True, base=TypedListType(allowed_type=RestrictedClassType(base_type=six.text_type, restriction_dict={u'pattern': u'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(/(([0-9])|([0-9]{2})|(1[0-1][0-9])|(12[0-8])))'})), is_leaf=False, yang_name="ipv6Address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://north-api.aliababa.com/schema/vlan/', defining_module='vlan_ip_schema', yang_type='inet:ipv6-prefix', is_config=True)

    load = kwargs.pop("load", None)
    if args:
      if len(args) > 1:
        raise TypeError("cannot create a YANG container with >1 argument")
      all_attr = True
      for e in self._pyangbind_elements:
        if not hasattr(args[0], e):
          all_attr = False
          break
      if not all_attr:
        raise ValueError("Supplied object did not have the correct attributes")
      for e in self._pyangbind_elements:
        nobj = getattr(args[0], e)
        if nobj._changed() is False:
          continue
        setmethod = getattr(self, "_set_%s" % e)
        if load is None:
          setmethod(getattr(args[0], e))
        else:
          setmethod(getattr(args[0], e), load=load)

  def _path(self):
    if hasattr(self, "_parent"):
      return self._parent._path()+[self._yang_name]
    else:
      return [u'VLAN_IP', u'ipAddress']

  def _get_ipv4Address(self):
    """
    Getter method for ipv4Address, mapped from YANG variable /VLAN_IP/ipAddress/ipv4Address (inet:ipv4-prefix)
    """
    return self.__ipv4Address
      
  def _set_ipv4Address(self, v, load=False):
    """
    Setter method for ipv4Address, mapped from YANG variable /VLAN_IP/ipAddress/ipv4Address (inet:ipv4-prefix)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ipv4Address is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ipv4Address() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,unique=True, base=TypedListType(allowed_type=RestrictedClassType(base_type=six.text_type, restriction_dict={u'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])/(([0-9])|([1-2][0-9])|(3[0-2]))'})), is_leaf=False, yang_name="ipv4Address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://north-api.aliababa.com/schema/vlan/', defining_module='vlan_ip_schema', yang_type='inet:ipv4-prefix', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ipv4Address must be of a type compatible with inet:ipv4-prefix""",
          'defined-type': "inet:ipv4-prefix",
          'generated-type': """YANGDynClass(unique=True, base=TypedListType(allowed_type=RestrictedClassType(base_type=six.text_type, restriction_dict={u'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])/(([0-9])|([1-2][0-9])|(3[0-2]))'})), is_leaf=False, yang_name="ipv4Address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://north-api.aliababa.com/schema/vlan/', defining_module='vlan_ip_schema', yang_type='inet:ipv4-prefix', is_config=True)""",
        })

    self.__ipv4Address = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ipv4Address(self):
    self.__ipv4Address = YANGDynClass(unique=True, base=TypedListType(allowed_type=RestrictedClassType(base_type=six.text_type, restriction_dict={u'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])/(([0-9])|([1-2][0-9])|(3[0-2]))'})), is_leaf=False, yang_name="ipv4Address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://north-api.aliababa.com/schema/vlan/', defining_module='vlan_ip_schema', yang_type='inet:ipv4-prefix', is_config=True)


  def _get_ipv6Address(self):
    """
    Getter method for ipv6Address, mapped from YANG variable /VLAN_IP/ipAddress/ipv6Address (inet:ipv6-prefix)
    """
    return self.__ipv6Address
      
  def _set_ipv6Address(self, v, load=False):
    """
    Setter method for ipv6Address, mapped from YANG variable /VLAN_IP/ipAddress/ipv6Address (inet:ipv6-prefix)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ipv6Address is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ipv6Address() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,unique=True, base=TypedListType(allowed_type=RestrictedClassType(base_type=six.text_type, restriction_dict={u'pattern': u'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(/(([0-9])|([0-9]{2})|(1[0-1][0-9])|(12[0-8])))'})), is_leaf=False, yang_name="ipv6Address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://north-api.aliababa.com/schema/vlan/', defining_module='vlan_ip_schema', yang_type='inet:ipv6-prefix', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ipv6Address must be of a type compatible with inet:ipv6-prefix""",
          'defined-type': "inet:ipv6-prefix",
          'generated-type': """YANGDynClass(unique=True, base=TypedListType(allowed_type=RestrictedClassType(base_type=six.text_type, restriction_dict={u'pattern': u'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(/(([0-9])|([0-9]{2})|(1[0-1][0-9])|(12[0-8])))'})), is_leaf=False, yang_name="ipv6Address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://north-api.aliababa.com/schema/vlan/', defining_module='vlan_ip_schema', yang_type='inet:ipv6-prefix', is_config=True)""",
        })

    self.__ipv6Address = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ipv6Address(self):
    self.__ipv6Address = YANGDynClass(unique=True, base=TypedListType(allowed_type=RestrictedClassType(base_type=six.text_type, restriction_dict={u'pattern': u'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(/(([0-9])|([0-9]{2})|(1[0-1][0-9])|(12[0-8])))'})), is_leaf=False, yang_name="ipv6Address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://north-api.aliababa.com/schema/vlan/', defining_module='vlan_ip_schema', yang_type='inet:ipv6-prefix', is_config=True)

  ipv4Address = __builtin__.property(_get_ipv4Address, _set_ipv4Address)
  ipv6Address = __builtin__.property(_get_ipv6Address, _set_ipv6Address)


  _pyangbind_elements = OrderedDict([('ipv4Address', ipv4Address), ('ipv6Address', ipv6Address), ])


class yc_VLAN_IP_vlan_ip_schema__VLAN_IP(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module vlan_ip_schema - based on the path /VLAN_IP. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_path_helper', '_extmethods', '__name__','__ipAddress',)

  _yang_name = 'VLAN_IP'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    helper = kwargs.pop("path_helper", None)
    if helper is False:
      self._path_helper = False
    elif helper is not None and isinstance(helper, xpathhelper.YANGPathHelper):
      self._path_helper = helper
    elif hasattr(self, "_parent"):
      helper = getattr(self._parent, "_path_helper", False)
      self._path_helper = helper
    else:
      self._path_helper = False

    self._extmethods = False
    self.__ipAddress = YANGDynClass(base=yc_ipAddress_vlan_ip_schema__VLAN_IP_ipAddress, is_container='container', yang_name="ipAddress", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://north-api.aliababa.com/schema/vlan/', defining_module='vlan_ip_schema', yang_type='container', is_config=True)
    self.__name__ = YANGDynClass(base=ReferenceType(referenced_path='/vlan-schema:VLAN/vlan-schema:name__', caller=self._path() + ['name__'], path_helper=self._path_helper, require_instance=True), is_leaf=True, yang_name="name__", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://north-api.aliababa.com/schema/vlan/', defining_module='vlan_ip_schema', yang_type='leafref', is_config=True)

    load = kwargs.pop("load", None)
    if args:
      if len(args) > 1:
        raise TypeError("cannot create a YANG container with >1 argument")
      all_attr = True
      for e in self._pyangbind_elements:
        if not hasattr(args[0], e):
          all_attr = False
          break
      if not all_attr:
        raise ValueError("Supplied object did not have the correct attributes")
      for e in self._pyangbind_elements:
        nobj = getattr(args[0], e)
        if nobj._changed() is False:
          continue
        setmethod = getattr(self, "_set_%s" % e)
        if load is None:
          setmethod(getattr(args[0], e))
        else:
          setmethod(getattr(args[0], e), load=load)

  def _path(self):
    if hasattr(self, "_parent"):
      return self._parent._path()+[self._yang_name]
    else:
      return [u'VLAN_IP']

  def _get_name__(self):
    """
    Getter method for name__, mapped from YANG variable /VLAN_IP/name__ (leafref)
    """
    return self.__name__
      
  def _set_name__(self, v, load=False):
    """
    Setter method for name__, mapped from YANG variable /VLAN_IP/name__ (leafref)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_name__ is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_name__() directly.
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=ReferenceType(referenced_path='/vlan-schema:VLAN/vlan-schema:name__', caller=self._path() + ['name__'], path_helper=self._path_helper, require_instance=True), is_leaf=True, yang_name="name__", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://north-api.aliababa.com/schema/vlan/', defining_module='vlan_ip_schema', yang_type='leafref', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """name__ must be of a type compatible with leafref""",
          'defined-type': "leafref",
          'generated-type': """YANGDynClass(base=ReferenceType(referenced_path='/vlan-schema:VLAN/vlan-schema:name__', caller=self._path() + ['name__'], path_helper=self._path_helper, require_instance=True), is_leaf=True, yang_name="name__", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://north-api.aliababa.com/schema/vlan/', defining_module='vlan_ip_schema', yang_type='leafref', is_config=True)""",
        })

    self.__name__ = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_name__(self):
    self.__name__ = YANGDynClass(base=ReferenceType(referenced_path='/vlan-schema:VLAN/vlan-schema:name__', caller=self._path() + ['name__'], path_helper=self._path_helper, require_instance=True), is_leaf=True, yang_name="name__", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://north-api.aliababa.com/schema/vlan/', defining_module='vlan_ip_schema', yang_type='leafref', is_config=True)


  def _get_ipAddress(self):
    """
    Getter method for ipAddress, mapped from YANG variable /VLAN_IP/ipAddress (container)
    """
    return self.__ipAddress
      
  def _set_ipAddress(self, v, load=False):
    """
    Setter method for ipAddress, mapped from YANG variable /VLAN_IP/ipAddress (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ipAddress is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ipAddress() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=yc_ipAddress_vlan_ip_schema__VLAN_IP_ipAddress, is_container='container', yang_name="ipAddress", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://north-api.aliababa.com/schema/vlan/', defining_module='vlan_ip_schema', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ipAddress must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=yc_ipAddress_vlan_ip_schema__VLAN_IP_ipAddress, is_container='container', yang_name="ipAddress", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://north-api.aliababa.com/schema/vlan/', defining_module='vlan_ip_schema', yang_type='container', is_config=True)""",
        })

    self.__ipAddress = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ipAddress(self):
    self.__ipAddress = YANGDynClass(base=yc_ipAddress_vlan_ip_schema__VLAN_IP_ipAddress, is_container='container', yang_name="ipAddress", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://north-api.aliababa.com/schema/vlan/', defining_module='vlan_ip_schema', yang_type='container', is_config=True)

  name__ = __builtin__.property(_get_name__, _set_name__)
  ipAddress = __builtin__.property(_get_ipAddress, _set_ipAddress)


  _pyangbind_elements = OrderedDict([('name__', name__), ('ipAddress', ipAddress), ])


class vlan_ip_schema(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module vlan_ip_schema - based on the path /vlan_ip_schema. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_path_helper', '_extmethods', '__VLAN_IP',)

  _yang_name = 'vlan_ip_schema'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    helper = kwargs.pop("path_helper", None)
    if helper is False:
      self._path_helper = False
    elif helper is not None and isinstance(helper, xpathhelper.YANGPathHelper):
      self._path_helper = helper
    elif hasattr(self, "_parent"):
      helper = getattr(self._parent, "_path_helper", False)
      self._path_helper = helper
    else:
      self._path_helper = False

    self._extmethods = False
    self.__VLAN_IP = YANGDynClass(base=YANGListType("name__",yc_VLAN_IP_vlan_ip_schema__VLAN_IP, yang_name="VLAN_IP", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='name__', extensions=None), is_container='list', yang_name="VLAN_IP", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://north-api.aliababa.com/schema/vlan/', defining_module='vlan_ip_schema', yang_type='list', is_config=True)

    load = kwargs.pop("load", None)
    if args:
      if len(args) > 1:
        raise TypeError("cannot create a YANG container with >1 argument")
      all_attr = True
      for e in self._pyangbind_elements:
        if not hasattr(args[0], e):
          all_attr = False
          break
      if not all_attr:
        raise ValueError("Supplied object did not have the correct attributes")
      for e in self._pyangbind_elements:
        nobj = getattr(args[0], e)
        if nobj._changed() is False:
          continue
        setmethod = getattr(self, "_set_%s" % e)
        if load is None:
          setmethod(getattr(args[0], e))
        else:
          setmethod(getattr(args[0], e), load=load)

  def _path(self):
    if hasattr(self, "_parent"):
      return self._parent._path()+[self._yang_name]
    else:
      return []

  def _get_VLAN_IP(self):
    """
    Getter method for VLAN_IP, mapped from YANG variable /VLAN_IP (list)
    """
    return self.__VLAN_IP
      
  def _set_VLAN_IP(self, v, load=False):
    """
    Setter method for VLAN_IP, mapped from YANG variable /VLAN_IP (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_VLAN_IP is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_VLAN_IP() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("name__",yc_VLAN_IP_vlan_ip_schema__VLAN_IP, yang_name="VLAN_IP", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='name__', extensions=None), is_container='list', yang_name="VLAN_IP", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://north-api.aliababa.com/schema/vlan/', defining_module='vlan_ip_schema', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """VLAN_IP must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("name__",yc_VLAN_IP_vlan_ip_schema__VLAN_IP, yang_name="VLAN_IP", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='name__', extensions=None), is_container='list', yang_name="VLAN_IP", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://north-api.aliababa.com/schema/vlan/', defining_module='vlan_ip_schema', yang_type='list', is_config=True)""",
        })

    self.__VLAN_IP = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_VLAN_IP(self):
    self.__VLAN_IP = YANGDynClass(base=YANGListType("name__",yc_VLAN_IP_vlan_ip_schema__VLAN_IP, yang_name="VLAN_IP", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='name__', extensions=None), is_container='list', yang_name="VLAN_IP", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://north-api.aliababa.com/schema/vlan/', defining_module='vlan_ip_schema', yang_type='list', is_config=True)

  VLAN_IP = __builtin__.property(_get_VLAN_IP, _set_VLAN_IP)


  _pyangbind_elements = OrderedDict([('VLAN_IP', VLAN_IP), ])


