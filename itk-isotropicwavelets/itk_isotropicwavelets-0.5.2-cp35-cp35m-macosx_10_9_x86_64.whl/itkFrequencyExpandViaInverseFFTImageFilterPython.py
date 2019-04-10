# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.8
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkFrequencyExpandViaInverseFFTImageFilterPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkFrequencyExpandViaInverseFFTImageFilterPython', [dirname(__file__)])
        except ImportError:
            import _itkFrequencyExpandViaInverseFFTImageFilterPython
            return _itkFrequencyExpandViaInverseFFTImageFilterPython
        if fp is not None:
            try:
                _mod = imp.load_module('_itkFrequencyExpandViaInverseFFTImageFilterPython', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _itkFrequencyExpandViaInverseFFTImageFilterPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkFrequencyExpandViaInverseFFTImageFilterPython
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
import itkFixedArrayPython
import itkImageToImageFilterBPython
import itkImageRegionPython
import itkSizePython
import itkIndexPython
import itkOffsetPython
import itkImageSourcePython
import itkImagePython
import itkSymmetricSecondRankTensorPython
import itkMatrixPython
import vnl_vectorPython
import vnl_matrixPython
import stdcomplexPython
import itkCovariantVectorPython
import vnl_vector_refPython
import itkVectorPython
import itkPointPython
import vnl_matrix_fixedPython
import itkRGBAPixelPython
import itkRGBPixelPython
import itkImageSourceCommonPython
import itkVectorImagePython
import itkVariableLengthVectorPython
import itkImageToImageFilterCommonPython

def itkFrequencyExpandViaInverseFFTImageFilterICF3_New():
  return itkFrequencyExpandViaInverseFFTImageFilterICF3.New()


def itkFrequencyExpandViaInverseFFTImageFilterICF2_New():
  return itkFrequencyExpandViaInverseFFTImageFilterICF2.New()

class itkFrequencyExpandViaInverseFFTImageFilterICF2(itkImageToImageFilterBPython.itkImageToImageFilterICF2ICF2):
    """Proxy of C++ itkFrequencyExpandViaInverseFFTImageFilterICF2 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkFrequencyExpandViaInverseFFTImageFilterICF2_Pointer":
        """__New_orig__() -> itkFrequencyExpandViaInverseFFTImageFilterICF2_Pointer"""
        return _itkFrequencyExpandViaInverseFFTImageFilterPython.itkFrequencyExpandViaInverseFFTImageFilterICF2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkFrequencyExpandViaInverseFFTImageFilterICF2_Pointer":
        """Clone(itkFrequencyExpandViaInverseFFTImageFilterICF2 self) -> itkFrequencyExpandViaInverseFFTImageFilterICF2_Pointer"""
        return _itkFrequencyExpandViaInverseFFTImageFilterPython.itkFrequencyExpandViaInverseFFTImageFilterICF2_Clone(self)


    def SetExpandFactors(self, *args) -> "void":
        """
        SetExpandFactors(itkFrequencyExpandViaInverseFFTImageFilterICF2 self, itkFixedArrayUI2 _arg)
        SetExpandFactors(itkFrequencyExpandViaInverseFFTImageFilterICF2 self, unsigned int const factor)
        """
        return _itkFrequencyExpandViaInverseFFTImageFilterPython.itkFrequencyExpandViaInverseFFTImageFilterICF2_SetExpandFactors(self, *args)


    def GetExpandFactors(self) -> "itkFixedArrayUI2 const &":
        """GetExpandFactors(itkFrequencyExpandViaInverseFFTImageFilterICF2 self) -> itkFixedArrayUI2"""
        return _itkFrequencyExpandViaInverseFFTImageFilterPython.itkFrequencyExpandViaInverseFFTImageFilterICF2_GetExpandFactors(self)


    def GenerateOutputInformation(self) -> "void":
        """GenerateOutputInformation(itkFrequencyExpandViaInverseFFTImageFilterICF2 self)"""
        return _itkFrequencyExpandViaInverseFFTImageFilterPython.itkFrequencyExpandViaInverseFFTImageFilterICF2_GenerateOutputInformation(self)


    def GenerateInputRequestedRegion(self) -> "void":
        """GenerateInputRequestedRegion(itkFrequencyExpandViaInverseFFTImageFilterICF2 self)"""
        return _itkFrequencyExpandViaInverseFFTImageFilterPython.itkFrequencyExpandViaInverseFFTImageFilterICF2_GenerateInputRequestedRegion(self)

    ImageTypeHasNumericTraitsCheck = _itkFrequencyExpandViaInverseFFTImageFilterPython.itkFrequencyExpandViaInverseFFTImageFilterICF2_ImageTypeHasNumericTraitsCheck
    __swig_destroy__ = _itkFrequencyExpandViaInverseFFTImageFilterPython.delete_itkFrequencyExpandViaInverseFFTImageFilterICF2

    def cast(obj: 'itkLightObject') -> "itkFrequencyExpandViaInverseFFTImageFilterICF2 *":
        """cast(itkLightObject obj) -> itkFrequencyExpandViaInverseFFTImageFilterICF2"""
        return _itkFrequencyExpandViaInverseFFTImageFilterPython.itkFrequencyExpandViaInverseFFTImageFilterICF2_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkFrequencyExpandViaInverseFFTImageFilterICF2

        Create a new object of the class itkFrequencyExpandViaInverseFFTImageFilterICF2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkFrequencyExpandViaInverseFFTImageFilterICF2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkFrequencyExpandViaInverseFFTImageFilterICF2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkFrequencyExpandViaInverseFFTImageFilterICF2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkFrequencyExpandViaInverseFFTImageFilterICF2.Clone = new_instancemethod(_itkFrequencyExpandViaInverseFFTImageFilterPython.itkFrequencyExpandViaInverseFFTImageFilterICF2_Clone, None, itkFrequencyExpandViaInverseFFTImageFilterICF2)
itkFrequencyExpandViaInverseFFTImageFilterICF2.SetExpandFactors = new_instancemethod(_itkFrequencyExpandViaInverseFFTImageFilterPython.itkFrequencyExpandViaInverseFFTImageFilterICF2_SetExpandFactors, None, itkFrequencyExpandViaInverseFFTImageFilterICF2)
itkFrequencyExpandViaInverseFFTImageFilterICF2.GetExpandFactors = new_instancemethod(_itkFrequencyExpandViaInverseFFTImageFilterPython.itkFrequencyExpandViaInverseFFTImageFilterICF2_GetExpandFactors, None, itkFrequencyExpandViaInverseFFTImageFilterICF2)
itkFrequencyExpandViaInverseFFTImageFilterICF2.GenerateOutputInformation = new_instancemethod(_itkFrequencyExpandViaInverseFFTImageFilterPython.itkFrequencyExpandViaInverseFFTImageFilterICF2_GenerateOutputInformation, None, itkFrequencyExpandViaInverseFFTImageFilterICF2)
itkFrequencyExpandViaInverseFFTImageFilterICF2.GenerateInputRequestedRegion = new_instancemethod(_itkFrequencyExpandViaInverseFFTImageFilterPython.itkFrequencyExpandViaInverseFFTImageFilterICF2_GenerateInputRequestedRegion, None, itkFrequencyExpandViaInverseFFTImageFilterICF2)
itkFrequencyExpandViaInverseFFTImageFilterICF2_swigregister = _itkFrequencyExpandViaInverseFFTImageFilterPython.itkFrequencyExpandViaInverseFFTImageFilterICF2_swigregister
itkFrequencyExpandViaInverseFFTImageFilterICF2_swigregister(itkFrequencyExpandViaInverseFFTImageFilterICF2)

def itkFrequencyExpandViaInverseFFTImageFilterICF2___New_orig__() -> "itkFrequencyExpandViaInverseFFTImageFilterICF2_Pointer":
    """itkFrequencyExpandViaInverseFFTImageFilterICF2___New_orig__() -> itkFrequencyExpandViaInverseFFTImageFilterICF2_Pointer"""
    return _itkFrequencyExpandViaInverseFFTImageFilterPython.itkFrequencyExpandViaInverseFFTImageFilterICF2___New_orig__()

def itkFrequencyExpandViaInverseFFTImageFilterICF2_cast(obj: 'itkLightObject') -> "itkFrequencyExpandViaInverseFFTImageFilterICF2 *":
    """itkFrequencyExpandViaInverseFFTImageFilterICF2_cast(itkLightObject obj) -> itkFrequencyExpandViaInverseFFTImageFilterICF2"""
    return _itkFrequencyExpandViaInverseFFTImageFilterPython.itkFrequencyExpandViaInverseFFTImageFilterICF2_cast(obj)

class itkFrequencyExpandViaInverseFFTImageFilterICF3(itkImageToImageFilterBPython.itkImageToImageFilterICF3ICF3):
    """Proxy of C++ itkFrequencyExpandViaInverseFFTImageFilterICF3 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkFrequencyExpandViaInverseFFTImageFilterICF3_Pointer":
        """__New_orig__() -> itkFrequencyExpandViaInverseFFTImageFilterICF3_Pointer"""
        return _itkFrequencyExpandViaInverseFFTImageFilterPython.itkFrequencyExpandViaInverseFFTImageFilterICF3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkFrequencyExpandViaInverseFFTImageFilterICF3_Pointer":
        """Clone(itkFrequencyExpandViaInverseFFTImageFilterICF3 self) -> itkFrequencyExpandViaInverseFFTImageFilterICF3_Pointer"""
        return _itkFrequencyExpandViaInverseFFTImageFilterPython.itkFrequencyExpandViaInverseFFTImageFilterICF3_Clone(self)


    def SetExpandFactors(self, *args) -> "void":
        """
        SetExpandFactors(itkFrequencyExpandViaInverseFFTImageFilterICF3 self, itkFixedArrayUI3 _arg)
        SetExpandFactors(itkFrequencyExpandViaInverseFFTImageFilterICF3 self, unsigned int const factor)
        """
        return _itkFrequencyExpandViaInverseFFTImageFilterPython.itkFrequencyExpandViaInverseFFTImageFilterICF3_SetExpandFactors(self, *args)


    def GetExpandFactors(self) -> "itkFixedArrayUI3 const &":
        """GetExpandFactors(itkFrequencyExpandViaInverseFFTImageFilterICF3 self) -> itkFixedArrayUI3"""
        return _itkFrequencyExpandViaInverseFFTImageFilterPython.itkFrequencyExpandViaInverseFFTImageFilterICF3_GetExpandFactors(self)


    def GenerateOutputInformation(self) -> "void":
        """GenerateOutputInformation(itkFrequencyExpandViaInverseFFTImageFilterICF3 self)"""
        return _itkFrequencyExpandViaInverseFFTImageFilterPython.itkFrequencyExpandViaInverseFFTImageFilterICF3_GenerateOutputInformation(self)


    def GenerateInputRequestedRegion(self) -> "void":
        """GenerateInputRequestedRegion(itkFrequencyExpandViaInverseFFTImageFilterICF3 self)"""
        return _itkFrequencyExpandViaInverseFFTImageFilterPython.itkFrequencyExpandViaInverseFFTImageFilterICF3_GenerateInputRequestedRegion(self)

    ImageTypeHasNumericTraitsCheck = _itkFrequencyExpandViaInverseFFTImageFilterPython.itkFrequencyExpandViaInverseFFTImageFilterICF3_ImageTypeHasNumericTraitsCheck
    __swig_destroy__ = _itkFrequencyExpandViaInverseFFTImageFilterPython.delete_itkFrequencyExpandViaInverseFFTImageFilterICF3

    def cast(obj: 'itkLightObject') -> "itkFrequencyExpandViaInverseFFTImageFilterICF3 *":
        """cast(itkLightObject obj) -> itkFrequencyExpandViaInverseFFTImageFilterICF3"""
        return _itkFrequencyExpandViaInverseFFTImageFilterPython.itkFrequencyExpandViaInverseFFTImageFilterICF3_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkFrequencyExpandViaInverseFFTImageFilterICF3

        Create a new object of the class itkFrequencyExpandViaInverseFFTImageFilterICF3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkFrequencyExpandViaInverseFFTImageFilterICF3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkFrequencyExpandViaInverseFFTImageFilterICF3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkFrequencyExpandViaInverseFFTImageFilterICF3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkFrequencyExpandViaInverseFFTImageFilterICF3.Clone = new_instancemethod(_itkFrequencyExpandViaInverseFFTImageFilterPython.itkFrequencyExpandViaInverseFFTImageFilterICF3_Clone, None, itkFrequencyExpandViaInverseFFTImageFilterICF3)
itkFrequencyExpandViaInverseFFTImageFilterICF3.SetExpandFactors = new_instancemethod(_itkFrequencyExpandViaInverseFFTImageFilterPython.itkFrequencyExpandViaInverseFFTImageFilterICF3_SetExpandFactors, None, itkFrequencyExpandViaInverseFFTImageFilterICF3)
itkFrequencyExpandViaInverseFFTImageFilterICF3.GetExpandFactors = new_instancemethod(_itkFrequencyExpandViaInverseFFTImageFilterPython.itkFrequencyExpandViaInverseFFTImageFilterICF3_GetExpandFactors, None, itkFrequencyExpandViaInverseFFTImageFilterICF3)
itkFrequencyExpandViaInverseFFTImageFilterICF3.GenerateOutputInformation = new_instancemethod(_itkFrequencyExpandViaInverseFFTImageFilterPython.itkFrequencyExpandViaInverseFFTImageFilterICF3_GenerateOutputInformation, None, itkFrequencyExpandViaInverseFFTImageFilterICF3)
itkFrequencyExpandViaInverseFFTImageFilterICF3.GenerateInputRequestedRegion = new_instancemethod(_itkFrequencyExpandViaInverseFFTImageFilterPython.itkFrequencyExpandViaInverseFFTImageFilterICF3_GenerateInputRequestedRegion, None, itkFrequencyExpandViaInverseFFTImageFilterICF3)
itkFrequencyExpandViaInverseFFTImageFilterICF3_swigregister = _itkFrequencyExpandViaInverseFFTImageFilterPython.itkFrequencyExpandViaInverseFFTImageFilterICF3_swigregister
itkFrequencyExpandViaInverseFFTImageFilterICF3_swigregister(itkFrequencyExpandViaInverseFFTImageFilterICF3)

def itkFrequencyExpandViaInverseFFTImageFilterICF3___New_orig__() -> "itkFrequencyExpandViaInverseFFTImageFilterICF3_Pointer":
    """itkFrequencyExpandViaInverseFFTImageFilterICF3___New_orig__() -> itkFrequencyExpandViaInverseFFTImageFilterICF3_Pointer"""
    return _itkFrequencyExpandViaInverseFFTImageFilterPython.itkFrequencyExpandViaInverseFFTImageFilterICF3___New_orig__()

def itkFrequencyExpandViaInverseFFTImageFilterICF3_cast(obj: 'itkLightObject') -> "itkFrequencyExpandViaInverseFFTImageFilterICF3 *":
    """itkFrequencyExpandViaInverseFFTImageFilterICF3_cast(itkLightObject obj) -> itkFrequencyExpandViaInverseFFTImageFilterICF3"""
    return _itkFrequencyExpandViaInverseFFTImageFilterPython.itkFrequencyExpandViaInverseFFTImageFilterICF3_cast(obj)


def frequency_expand_via_inverse_fft_image_filter(*args, **kwargs):
    """Procedural interface for FrequencyExpandViaInverseFFTImageFilter"""
    import itk
    return itk.FrequencyExpandViaInverseFFTImageFilter.__call__(*args, **kwargs)



