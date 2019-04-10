# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.8
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkShannonIsotropicWaveletPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkShannonIsotropicWaveletPython', [dirname(__file__)])
        except ImportError:
            import _itkShannonIsotropicWaveletPython
            return _itkShannonIsotropicWaveletPython
        if fp is not None:
            try:
                _mod = imp.load_module('_itkShannonIsotropicWaveletPython', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _itkShannonIsotropicWaveletPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkShannonIsotropicWaveletPython
del version_info
try:
    _swig_property = property
except NameError:
    pass  # Python < 2.2 doesn't have 'property'.


def _swig_setattr_nondynamic(self, class_type, name, value, static=1):
    if (name == "thisown"):
        return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name, None)
    if method:
        return method(self, value)
    if (not static):
        object.__setattr__(self, name, value)
    else:
        raise AttributeError("You cannot add attributes to %s" % self)


def _swig_setattr(self, class_type, name, value):
    return _swig_setattr_nondynamic(self, class_type, name, value, 0)


def _swig_getattr_nondynamic(self, class_type, name, static=1):
    if (name == "thisown"):
        return self.this.own()
    method = class_type.__swig_getmethods__.get(name, None)
    if method:
        return method(self)
    if (not static):
        return object.__getattr__(self, name)
    else:
        raise AttributeError(name)

def _swig_getattr(self, class_type, name):
    return _swig_getattr_nondynamic(self, class_type, name, 0)


def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object:
        pass
    _newclass = 0



def _swig_setattr_nondynamic_method(set):
    def set_attr(self, name, value):
        if (name == "thisown"):
            return self.this.own(value)
        if hasattr(self, name) or (name == "this"):
            set(self, name, value)
        else:
            raise AttributeError("You cannot add attributes to %s" % self)
    return set_attr


import itkIsotropicWaveletFrequencyFunctionPython
import ITKCommonBasePython
import pyBasePython
import itkIsotropicFrequencyFunctionPython
import itkFrequencyFunctionPython
import itkSpatialFunctionPython
import itkFunctionBasePython
import itkRGBAPixelPython
import itkFixedArrayPython
import itkVectorPython
import vnl_vector_refPython
import vnl_vectorPython
import vnl_matrixPython
import stdcomplexPython
import itkRGBPixelPython
import itkImagePython
import itkMatrixPython
import vnl_matrix_fixedPython
import itkPointPython
import itkCovariantVectorPython
import itkOffsetPython
import itkSizePython
import itkIndexPython
import itkSymmetricSecondRankTensorPython
import itkImageRegionPython
import itkContinuousIndexPython
import itkArrayPython

def itkShannonIsotropicWaveletF3PD3_New():
  return itkShannonIsotropicWaveletF3PD3.New()


def itkShannonIsotropicWaveletF2PD2_New():
  return itkShannonIsotropicWaveletF2PD2.New()

class itkShannonIsotropicWaveletF2PD2(itkIsotropicWaveletFrequencyFunctionPython.itkIsotropicWaveletFrequencyFunctionF2PD2):
    """Proxy of C++ itkShannonIsotropicWaveletF2PD2 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkShannonIsotropicWaveletF2PD2_Pointer":
        """__New_orig__() -> itkShannonIsotropicWaveletF2PD2_Pointer"""
        return _itkShannonIsotropicWaveletPython.itkShannonIsotropicWaveletF2PD2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkShannonIsotropicWaveletF2PD2_Pointer":
        """Clone(itkShannonIsotropicWaveletF2PD2 self) -> itkShannonIsotropicWaveletF2PD2_Pointer"""
        return _itkShannonIsotropicWaveletPython.itkShannonIsotropicWaveletF2PD2_Clone(self)

    __swig_destroy__ = _itkShannonIsotropicWaveletPython.delete_itkShannonIsotropicWaveletF2PD2

    def cast(obj: 'itkLightObject') -> "itkShannonIsotropicWaveletF2PD2 *":
        """cast(itkLightObject obj) -> itkShannonIsotropicWaveletF2PD2"""
        return _itkShannonIsotropicWaveletPython.itkShannonIsotropicWaveletF2PD2_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkShannonIsotropicWaveletF2PD2

        Create a new object of the class itkShannonIsotropicWaveletF2PD2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkShannonIsotropicWaveletF2PD2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkShannonIsotropicWaveletF2PD2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkShannonIsotropicWaveletF2PD2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkShannonIsotropicWaveletF2PD2.Clone = new_instancemethod(_itkShannonIsotropicWaveletPython.itkShannonIsotropicWaveletF2PD2_Clone, None, itkShannonIsotropicWaveletF2PD2)
itkShannonIsotropicWaveletF2PD2_swigregister = _itkShannonIsotropicWaveletPython.itkShannonIsotropicWaveletF2PD2_swigregister
itkShannonIsotropicWaveletF2PD2_swigregister(itkShannonIsotropicWaveletF2PD2)

def itkShannonIsotropicWaveletF2PD2___New_orig__() -> "itkShannonIsotropicWaveletF2PD2_Pointer":
    """itkShannonIsotropicWaveletF2PD2___New_orig__() -> itkShannonIsotropicWaveletF2PD2_Pointer"""
    return _itkShannonIsotropicWaveletPython.itkShannonIsotropicWaveletF2PD2___New_orig__()

def itkShannonIsotropicWaveletF2PD2_cast(obj: 'itkLightObject') -> "itkShannonIsotropicWaveletF2PD2 *":
    """itkShannonIsotropicWaveletF2PD2_cast(itkLightObject obj) -> itkShannonIsotropicWaveletF2PD2"""
    return _itkShannonIsotropicWaveletPython.itkShannonIsotropicWaveletF2PD2_cast(obj)

class itkShannonIsotropicWaveletF3PD3(itkIsotropicWaveletFrequencyFunctionPython.itkIsotropicWaveletFrequencyFunctionF3PD3):
    """Proxy of C++ itkShannonIsotropicWaveletF3PD3 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkShannonIsotropicWaveletF3PD3_Pointer":
        """__New_orig__() -> itkShannonIsotropicWaveletF3PD3_Pointer"""
        return _itkShannonIsotropicWaveletPython.itkShannonIsotropicWaveletF3PD3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkShannonIsotropicWaveletF3PD3_Pointer":
        """Clone(itkShannonIsotropicWaveletF3PD3 self) -> itkShannonIsotropicWaveletF3PD3_Pointer"""
        return _itkShannonIsotropicWaveletPython.itkShannonIsotropicWaveletF3PD3_Clone(self)

    __swig_destroy__ = _itkShannonIsotropicWaveletPython.delete_itkShannonIsotropicWaveletF3PD3

    def cast(obj: 'itkLightObject') -> "itkShannonIsotropicWaveletF3PD3 *":
        """cast(itkLightObject obj) -> itkShannonIsotropicWaveletF3PD3"""
        return _itkShannonIsotropicWaveletPython.itkShannonIsotropicWaveletF3PD3_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkShannonIsotropicWaveletF3PD3

        Create a new object of the class itkShannonIsotropicWaveletF3PD3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkShannonIsotropicWaveletF3PD3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkShannonIsotropicWaveletF3PD3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkShannonIsotropicWaveletF3PD3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkShannonIsotropicWaveletF3PD3.Clone = new_instancemethod(_itkShannonIsotropicWaveletPython.itkShannonIsotropicWaveletF3PD3_Clone, None, itkShannonIsotropicWaveletF3PD3)
itkShannonIsotropicWaveletF3PD3_swigregister = _itkShannonIsotropicWaveletPython.itkShannonIsotropicWaveletF3PD3_swigregister
itkShannonIsotropicWaveletF3PD3_swigregister(itkShannonIsotropicWaveletF3PD3)

def itkShannonIsotropicWaveletF3PD3___New_orig__() -> "itkShannonIsotropicWaveletF3PD3_Pointer":
    """itkShannonIsotropicWaveletF3PD3___New_orig__() -> itkShannonIsotropicWaveletF3PD3_Pointer"""
    return _itkShannonIsotropicWaveletPython.itkShannonIsotropicWaveletF3PD3___New_orig__()

def itkShannonIsotropicWaveletF3PD3_cast(obj: 'itkLightObject') -> "itkShannonIsotropicWaveletF3PD3 *":
    """itkShannonIsotropicWaveletF3PD3_cast(itkLightObject obj) -> itkShannonIsotropicWaveletF3PD3"""
    return _itkShannonIsotropicWaveletPython.itkShannonIsotropicWaveletF3PD3_cast(obj)



