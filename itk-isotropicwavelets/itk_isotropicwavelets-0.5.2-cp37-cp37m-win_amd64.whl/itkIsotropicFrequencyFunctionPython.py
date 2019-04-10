# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.8
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkIsotropicFrequencyFunctionPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkIsotropicFrequencyFunctionPython', [dirname(__file__)])
        except ImportError:
            import _itkIsotropicFrequencyFunctionPython
            return _itkIsotropicFrequencyFunctionPython
        if fp is not None:
            try:
                _mod = imp.load_module('_itkIsotropicFrequencyFunctionPython', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _itkIsotropicFrequencyFunctionPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkIsotropicFrequencyFunctionPython
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


import ITKCommonBasePython
import pyBasePython
import itkPointPython
import vnl_vector_refPython
import stdcomplexPython
import vnl_vectorPython
import vnl_matrixPython
import itkVectorPython
import itkFixedArrayPython
import itkFrequencyFunctionPython
import itkSpatialFunctionPython
import itkFunctionBasePython
import itkCovariantVectorPython
import itkContinuousIndexPython
import itkIndexPython
import itkOffsetPython
import itkSizePython
import itkRGBAPixelPython
import itkRGBPixelPython
import itkImagePython
import itkSymmetricSecondRankTensorPython
import itkMatrixPython
import vnl_matrix_fixedPython
import itkImageRegionPython
import itkArrayPython

def itkIsotropicFrequencyFunctionF3PD3_New():
  return itkIsotropicFrequencyFunctionF3PD3.New()


def itkIsotropicFrequencyFunctionF2PD2_New():
  return itkIsotropicFrequencyFunctionF2PD2.New()

class itkIsotropicFrequencyFunctionF2PD2(itkFrequencyFunctionPython.itkFrequencyFunctionF2PD2):
    """Proxy of C++ itkIsotropicFrequencyFunctionF2PD2 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr

    def Magnitude(self, point: 'itkPointD2') -> "double":
        """Magnitude(itkIsotropicFrequencyFunctionF2PD2 self, itkPointD2 point) -> double"""
        return _itkIsotropicFrequencyFunctionPython.itkIsotropicFrequencyFunctionF2PD2_Magnitude(self, point)


    def EvaluateMagnitude(self, freq_norm_in_hz: 'float const &') -> "float":
        """EvaluateMagnitude(itkIsotropicFrequencyFunctionF2PD2 self, float const & freq_norm_in_hz) -> float"""
        return _itkIsotropicFrequencyFunctionPython.itkIsotropicFrequencyFunctionF2PD2_EvaluateMagnitude(self, freq_norm_in_hz)

    __swig_destroy__ = _itkIsotropicFrequencyFunctionPython.delete_itkIsotropicFrequencyFunctionF2PD2

    def cast(obj: 'itkLightObject') -> "itkIsotropicFrequencyFunctionF2PD2 *":
        """cast(itkLightObject obj) -> itkIsotropicFrequencyFunctionF2PD2"""
        return _itkIsotropicFrequencyFunctionPython.itkIsotropicFrequencyFunctionF2PD2_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkIsotropicFrequencyFunctionF2PD2

        Create a new object of the class itkIsotropicFrequencyFunctionF2PD2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkIsotropicFrequencyFunctionF2PD2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkIsotropicFrequencyFunctionF2PD2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkIsotropicFrequencyFunctionF2PD2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkIsotropicFrequencyFunctionF2PD2.Magnitude = new_instancemethod(_itkIsotropicFrequencyFunctionPython.itkIsotropicFrequencyFunctionF2PD2_Magnitude, None, itkIsotropicFrequencyFunctionF2PD2)
itkIsotropicFrequencyFunctionF2PD2.EvaluateMagnitude = new_instancemethod(_itkIsotropicFrequencyFunctionPython.itkIsotropicFrequencyFunctionF2PD2_EvaluateMagnitude, None, itkIsotropicFrequencyFunctionF2PD2)
itkIsotropicFrequencyFunctionF2PD2_swigregister = _itkIsotropicFrequencyFunctionPython.itkIsotropicFrequencyFunctionF2PD2_swigregister
itkIsotropicFrequencyFunctionF2PD2_swigregister(itkIsotropicFrequencyFunctionF2PD2)

def itkIsotropicFrequencyFunctionF2PD2_cast(obj: 'itkLightObject') -> "itkIsotropicFrequencyFunctionF2PD2 *":
    """itkIsotropicFrequencyFunctionF2PD2_cast(itkLightObject obj) -> itkIsotropicFrequencyFunctionF2PD2"""
    return _itkIsotropicFrequencyFunctionPython.itkIsotropicFrequencyFunctionF2PD2_cast(obj)

class itkIsotropicFrequencyFunctionF3PD3(itkFrequencyFunctionPython.itkFrequencyFunctionF3PD3):
    """Proxy of C++ itkIsotropicFrequencyFunctionF3PD3 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr

    def Magnitude(self, point: 'itkPointD3') -> "double":
        """Magnitude(itkIsotropicFrequencyFunctionF3PD3 self, itkPointD3 point) -> double"""
        return _itkIsotropicFrequencyFunctionPython.itkIsotropicFrequencyFunctionF3PD3_Magnitude(self, point)


    def EvaluateMagnitude(self, freq_norm_in_hz: 'float const &') -> "float":
        """EvaluateMagnitude(itkIsotropicFrequencyFunctionF3PD3 self, float const & freq_norm_in_hz) -> float"""
        return _itkIsotropicFrequencyFunctionPython.itkIsotropicFrequencyFunctionF3PD3_EvaluateMagnitude(self, freq_norm_in_hz)

    __swig_destroy__ = _itkIsotropicFrequencyFunctionPython.delete_itkIsotropicFrequencyFunctionF3PD3

    def cast(obj: 'itkLightObject') -> "itkIsotropicFrequencyFunctionF3PD3 *":
        """cast(itkLightObject obj) -> itkIsotropicFrequencyFunctionF3PD3"""
        return _itkIsotropicFrequencyFunctionPython.itkIsotropicFrequencyFunctionF3PD3_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkIsotropicFrequencyFunctionF3PD3

        Create a new object of the class itkIsotropicFrequencyFunctionF3PD3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkIsotropicFrequencyFunctionF3PD3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkIsotropicFrequencyFunctionF3PD3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkIsotropicFrequencyFunctionF3PD3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkIsotropicFrequencyFunctionF3PD3.Magnitude = new_instancemethod(_itkIsotropicFrequencyFunctionPython.itkIsotropicFrequencyFunctionF3PD3_Magnitude, None, itkIsotropicFrequencyFunctionF3PD3)
itkIsotropicFrequencyFunctionF3PD3.EvaluateMagnitude = new_instancemethod(_itkIsotropicFrequencyFunctionPython.itkIsotropicFrequencyFunctionF3PD3_EvaluateMagnitude, None, itkIsotropicFrequencyFunctionF3PD3)
itkIsotropicFrequencyFunctionF3PD3_swigregister = _itkIsotropicFrequencyFunctionPython.itkIsotropicFrequencyFunctionF3PD3_swigregister
itkIsotropicFrequencyFunctionF3PD3_swigregister(itkIsotropicFrequencyFunctionF3PD3)

def itkIsotropicFrequencyFunctionF3PD3_cast(obj: 'itkLightObject') -> "itkIsotropicFrequencyFunctionF3PD3 *":
    """itkIsotropicFrequencyFunctionF3PD3_cast(itkLightObject obj) -> itkIsotropicFrequencyFunctionF3PD3"""
    return _itkIsotropicFrequencyFunctionPython.itkIsotropicFrequencyFunctionF3PD3_cast(obj)



