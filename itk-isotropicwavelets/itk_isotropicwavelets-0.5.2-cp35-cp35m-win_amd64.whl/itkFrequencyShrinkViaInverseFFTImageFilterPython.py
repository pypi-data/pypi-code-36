# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.8
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkFrequencyShrinkViaInverseFFTImageFilterPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkFrequencyShrinkViaInverseFFTImageFilterPython', [dirname(__file__)])
        except ImportError:
            import _itkFrequencyShrinkViaInverseFFTImageFilterPython
            return _itkFrequencyShrinkViaInverseFFTImageFilterPython
        if fp is not None:
            try:
                _mod = imp.load_module('_itkFrequencyShrinkViaInverseFFTImageFilterPython', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _itkFrequencyShrinkViaInverseFFTImageFilterPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkFrequencyShrinkViaInverseFFTImageFilterPython
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


import itkImageToImageFilterBPython
import ITKCommonBasePython
import pyBasePython
import itkImageSourcePython
import itkVectorImagePython
import itkIndexPython
import itkSizePython
import itkOffsetPython
import stdcomplexPython
import itkImagePython
import itkFixedArrayPython
import itkRGBAPixelPython
import itkRGBPixelPython
import itkPointPython
import vnl_vector_refPython
import vnl_vectorPython
import vnl_matrixPython
import itkVectorPython
import itkImageRegionPython
import itkMatrixPython
import vnl_matrix_fixedPython
import itkCovariantVectorPython
import itkSymmetricSecondRankTensorPython
import itkVariableLengthVectorPython
import itkImageSourceCommonPython
import itkImageToImageFilterCommonPython

def itkFrequencyShrinkViaInverseFFTImageFilterICF3_New():
  return itkFrequencyShrinkViaInverseFFTImageFilterICF3.New()


def itkFrequencyShrinkViaInverseFFTImageFilterICF2_New():
  return itkFrequencyShrinkViaInverseFFTImageFilterICF2.New()

class itkFrequencyShrinkViaInverseFFTImageFilterICF2(itkImageToImageFilterBPython.itkImageToImageFilterICF2ICF2):
    """Proxy of C++ itkFrequencyShrinkViaInverseFFTImageFilterICF2 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkFrequencyShrinkViaInverseFFTImageFilterICF2_Pointer":
        """__New_orig__() -> itkFrequencyShrinkViaInverseFFTImageFilterICF2_Pointer"""
        return _itkFrequencyShrinkViaInverseFFTImageFilterPython.itkFrequencyShrinkViaInverseFFTImageFilterICF2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkFrequencyShrinkViaInverseFFTImageFilterICF2_Pointer":
        """Clone(itkFrequencyShrinkViaInverseFFTImageFilterICF2 self) -> itkFrequencyShrinkViaInverseFFTImageFilterICF2_Pointer"""
        return _itkFrequencyShrinkViaInverseFFTImageFilterPython.itkFrequencyShrinkViaInverseFFTImageFilterICF2_Clone(self)


    def SetShrinkFactors(self, *args) -> "void":
        """
        SetShrinkFactors(itkFrequencyShrinkViaInverseFFTImageFilterICF2 self, itkFixedArrayUI2 _arg)
        SetShrinkFactors(itkFrequencyShrinkViaInverseFFTImageFilterICF2 self, unsigned int factor)
        """
        return _itkFrequencyShrinkViaInverseFFTImageFilterPython.itkFrequencyShrinkViaInverseFFTImageFilterICF2_SetShrinkFactors(self, *args)


    def SetShrinkFactor(self, i: 'unsigned int', factor: 'unsigned int') -> "void":
        """SetShrinkFactor(itkFrequencyShrinkViaInverseFFTImageFilterICF2 self, unsigned int i, unsigned int factor)"""
        return _itkFrequencyShrinkViaInverseFFTImageFilterPython.itkFrequencyShrinkViaInverseFFTImageFilterICF2_SetShrinkFactor(self, i, factor)


    def GetShrinkFactors(self) -> "itkFixedArrayUI2 const &":
        """GetShrinkFactors(itkFrequencyShrinkViaInverseFFTImageFilterICF2 self) -> itkFixedArrayUI2"""
        return _itkFrequencyShrinkViaInverseFFTImageFilterPython.itkFrequencyShrinkViaInverseFFTImageFilterICF2_GetShrinkFactors(self)


    def GenerateOutputInformation(self) -> "void":
        """GenerateOutputInformation(itkFrequencyShrinkViaInverseFFTImageFilterICF2 self)"""
        return _itkFrequencyShrinkViaInverseFFTImageFilterPython.itkFrequencyShrinkViaInverseFFTImageFilterICF2_GenerateOutputInformation(self)


    def GenerateInputRequestedRegion(self) -> "void":
        """GenerateInputRequestedRegion(itkFrequencyShrinkViaInverseFFTImageFilterICF2 self)"""
        return _itkFrequencyShrinkViaInverseFFTImageFilterPython.itkFrequencyShrinkViaInverseFFTImageFilterICF2_GenerateInputRequestedRegion(self)

    ImageTypeHasNumericTraitsCheck = _itkFrequencyShrinkViaInverseFFTImageFilterPython.itkFrequencyShrinkViaInverseFFTImageFilterICF2_ImageTypeHasNumericTraitsCheck
    __swig_destroy__ = _itkFrequencyShrinkViaInverseFFTImageFilterPython.delete_itkFrequencyShrinkViaInverseFFTImageFilterICF2

    def cast(obj: 'itkLightObject') -> "itkFrequencyShrinkViaInverseFFTImageFilterICF2 *":
        """cast(itkLightObject obj) -> itkFrequencyShrinkViaInverseFFTImageFilterICF2"""
        return _itkFrequencyShrinkViaInverseFFTImageFilterPython.itkFrequencyShrinkViaInverseFFTImageFilterICF2_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkFrequencyShrinkViaInverseFFTImageFilterICF2

        Create a new object of the class itkFrequencyShrinkViaInverseFFTImageFilterICF2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkFrequencyShrinkViaInverseFFTImageFilterICF2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkFrequencyShrinkViaInverseFFTImageFilterICF2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkFrequencyShrinkViaInverseFFTImageFilterICF2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkFrequencyShrinkViaInverseFFTImageFilterICF2.Clone = new_instancemethod(_itkFrequencyShrinkViaInverseFFTImageFilterPython.itkFrequencyShrinkViaInverseFFTImageFilterICF2_Clone, None, itkFrequencyShrinkViaInverseFFTImageFilterICF2)
itkFrequencyShrinkViaInverseFFTImageFilterICF2.SetShrinkFactors = new_instancemethod(_itkFrequencyShrinkViaInverseFFTImageFilterPython.itkFrequencyShrinkViaInverseFFTImageFilterICF2_SetShrinkFactors, None, itkFrequencyShrinkViaInverseFFTImageFilterICF2)
itkFrequencyShrinkViaInverseFFTImageFilterICF2.SetShrinkFactor = new_instancemethod(_itkFrequencyShrinkViaInverseFFTImageFilterPython.itkFrequencyShrinkViaInverseFFTImageFilterICF2_SetShrinkFactor, None, itkFrequencyShrinkViaInverseFFTImageFilterICF2)
itkFrequencyShrinkViaInverseFFTImageFilterICF2.GetShrinkFactors = new_instancemethod(_itkFrequencyShrinkViaInverseFFTImageFilterPython.itkFrequencyShrinkViaInverseFFTImageFilterICF2_GetShrinkFactors, None, itkFrequencyShrinkViaInverseFFTImageFilterICF2)
itkFrequencyShrinkViaInverseFFTImageFilterICF2.GenerateOutputInformation = new_instancemethod(_itkFrequencyShrinkViaInverseFFTImageFilterPython.itkFrequencyShrinkViaInverseFFTImageFilterICF2_GenerateOutputInformation, None, itkFrequencyShrinkViaInverseFFTImageFilterICF2)
itkFrequencyShrinkViaInverseFFTImageFilterICF2.GenerateInputRequestedRegion = new_instancemethod(_itkFrequencyShrinkViaInverseFFTImageFilterPython.itkFrequencyShrinkViaInverseFFTImageFilterICF2_GenerateInputRequestedRegion, None, itkFrequencyShrinkViaInverseFFTImageFilterICF2)
itkFrequencyShrinkViaInverseFFTImageFilterICF2_swigregister = _itkFrequencyShrinkViaInverseFFTImageFilterPython.itkFrequencyShrinkViaInverseFFTImageFilterICF2_swigregister
itkFrequencyShrinkViaInverseFFTImageFilterICF2_swigregister(itkFrequencyShrinkViaInverseFFTImageFilterICF2)

def itkFrequencyShrinkViaInverseFFTImageFilterICF2___New_orig__() -> "itkFrequencyShrinkViaInverseFFTImageFilterICF2_Pointer":
    """itkFrequencyShrinkViaInverseFFTImageFilterICF2___New_orig__() -> itkFrequencyShrinkViaInverseFFTImageFilterICF2_Pointer"""
    return _itkFrequencyShrinkViaInverseFFTImageFilterPython.itkFrequencyShrinkViaInverseFFTImageFilterICF2___New_orig__()

def itkFrequencyShrinkViaInverseFFTImageFilterICF2_cast(obj: 'itkLightObject') -> "itkFrequencyShrinkViaInverseFFTImageFilterICF2 *":
    """itkFrequencyShrinkViaInverseFFTImageFilterICF2_cast(itkLightObject obj) -> itkFrequencyShrinkViaInverseFFTImageFilterICF2"""
    return _itkFrequencyShrinkViaInverseFFTImageFilterPython.itkFrequencyShrinkViaInverseFFTImageFilterICF2_cast(obj)

class itkFrequencyShrinkViaInverseFFTImageFilterICF3(itkImageToImageFilterBPython.itkImageToImageFilterICF3ICF3):
    """Proxy of C++ itkFrequencyShrinkViaInverseFFTImageFilterICF3 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkFrequencyShrinkViaInverseFFTImageFilterICF3_Pointer":
        """__New_orig__() -> itkFrequencyShrinkViaInverseFFTImageFilterICF3_Pointer"""
        return _itkFrequencyShrinkViaInverseFFTImageFilterPython.itkFrequencyShrinkViaInverseFFTImageFilterICF3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkFrequencyShrinkViaInverseFFTImageFilterICF3_Pointer":
        """Clone(itkFrequencyShrinkViaInverseFFTImageFilterICF3 self) -> itkFrequencyShrinkViaInverseFFTImageFilterICF3_Pointer"""
        return _itkFrequencyShrinkViaInverseFFTImageFilterPython.itkFrequencyShrinkViaInverseFFTImageFilterICF3_Clone(self)


    def SetShrinkFactors(self, *args) -> "void":
        """
        SetShrinkFactors(itkFrequencyShrinkViaInverseFFTImageFilterICF3 self, itkFixedArrayUI3 _arg)
        SetShrinkFactors(itkFrequencyShrinkViaInverseFFTImageFilterICF3 self, unsigned int factor)
        """
        return _itkFrequencyShrinkViaInverseFFTImageFilterPython.itkFrequencyShrinkViaInverseFFTImageFilterICF3_SetShrinkFactors(self, *args)


    def SetShrinkFactor(self, i: 'unsigned int', factor: 'unsigned int') -> "void":
        """SetShrinkFactor(itkFrequencyShrinkViaInverseFFTImageFilterICF3 self, unsigned int i, unsigned int factor)"""
        return _itkFrequencyShrinkViaInverseFFTImageFilterPython.itkFrequencyShrinkViaInverseFFTImageFilterICF3_SetShrinkFactor(self, i, factor)


    def GetShrinkFactors(self) -> "itkFixedArrayUI3 const &":
        """GetShrinkFactors(itkFrequencyShrinkViaInverseFFTImageFilterICF3 self) -> itkFixedArrayUI3"""
        return _itkFrequencyShrinkViaInverseFFTImageFilterPython.itkFrequencyShrinkViaInverseFFTImageFilterICF3_GetShrinkFactors(self)


    def GenerateOutputInformation(self) -> "void":
        """GenerateOutputInformation(itkFrequencyShrinkViaInverseFFTImageFilterICF3 self)"""
        return _itkFrequencyShrinkViaInverseFFTImageFilterPython.itkFrequencyShrinkViaInverseFFTImageFilterICF3_GenerateOutputInformation(self)


    def GenerateInputRequestedRegion(self) -> "void":
        """GenerateInputRequestedRegion(itkFrequencyShrinkViaInverseFFTImageFilterICF3 self)"""
        return _itkFrequencyShrinkViaInverseFFTImageFilterPython.itkFrequencyShrinkViaInverseFFTImageFilterICF3_GenerateInputRequestedRegion(self)

    ImageTypeHasNumericTraitsCheck = _itkFrequencyShrinkViaInverseFFTImageFilterPython.itkFrequencyShrinkViaInverseFFTImageFilterICF3_ImageTypeHasNumericTraitsCheck
    __swig_destroy__ = _itkFrequencyShrinkViaInverseFFTImageFilterPython.delete_itkFrequencyShrinkViaInverseFFTImageFilterICF3

    def cast(obj: 'itkLightObject') -> "itkFrequencyShrinkViaInverseFFTImageFilterICF3 *":
        """cast(itkLightObject obj) -> itkFrequencyShrinkViaInverseFFTImageFilterICF3"""
        return _itkFrequencyShrinkViaInverseFFTImageFilterPython.itkFrequencyShrinkViaInverseFFTImageFilterICF3_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkFrequencyShrinkViaInverseFFTImageFilterICF3

        Create a new object of the class itkFrequencyShrinkViaInverseFFTImageFilterICF3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkFrequencyShrinkViaInverseFFTImageFilterICF3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkFrequencyShrinkViaInverseFFTImageFilterICF3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkFrequencyShrinkViaInverseFFTImageFilterICF3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkFrequencyShrinkViaInverseFFTImageFilterICF3.Clone = new_instancemethod(_itkFrequencyShrinkViaInverseFFTImageFilterPython.itkFrequencyShrinkViaInverseFFTImageFilterICF3_Clone, None, itkFrequencyShrinkViaInverseFFTImageFilterICF3)
itkFrequencyShrinkViaInverseFFTImageFilterICF3.SetShrinkFactors = new_instancemethod(_itkFrequencyShrinkViaInverseFFTImageFilterPython.itkFrequencyShrinkViaInverseFFTImageFilterICF3_SetShrinkFactors, None, itkFrequencyShrinkViaInverseFFTImageFilterICF3)
itkFrequencyShrinkViaInverseFFTImageFilterICF3.SetShrinkFactor = new_instancemethod(_itkFrequencyShrinkViaInverseFFTImageFilterPython.itkFrequencyShrinkViaInverseFFTImageFilterICF3_SetShrinkFactor, None, itkFrequencyShrinkViaInverseFFTImageFilterICF3)
itkFrequencyShrinkViaInverseFFTImageFilterICF3.GetShrinkFactors = new_instancemethod(_itkFrequencyShrinkViaInverseFFTImageFilterPython.itkFrequencyShrinkViaInverseFFTImageFilterICF3_GetShrinkFactors, None, itkFrequencyShrinkViaInverseFFTImageFilterICF3)
itkFrequencyShrinkViaInverseFFTImageFilterICF3.GenerateOutputInformation = new_instancemethod(_itkFrequencyShrinkViaInverseFFTImageFilterPython.itkFrequencyShrinkViaInverseFFTImageFilterICF3_GenerateOutputInformation, None, itkFrequencyShrinkViaInverseFFTImageFilterICF3)
itkFrequencyShrinkViaInverseFFTImageFilterICF3.GenerateInputRequestedRegion = new_instancemethod(_itkFrequencyShrinkViaInverseFFTImageFilterPython.itkFrequencyShrinkViaInverseFFTImageFilterICF3_GenerateInputRequestedRegion, None, itkFrequencyShrinkViaInverseFFTImageFilterICF3)
itkFrequencyShrinkViaInverseFFTImageFilterICF3_swigregister = _itkFrequencyShrinkViaInverseFFTImageFilterPython.itkFrequencyShrinkViaInverseFFTImageFilterICF3_swigregister
itkFrequencyShrinkViaInverseFFTImageFilterICF3_swigregister(itkFrequencyShrinkViaInverseFFTImageFilterICF3)

def itkFrequencyShrinkViaInverseFFTImageFilterICF3___New_orig__() -> "itkFrequencyShrinkViaInverseFFTImageFilterICF3_Pointer":
    """itkFrequencyShrinkViaInverseFFTImageFilterICF3___New_orig__() -> itkFrequencyShrinkViaInverseFFTImageFilterICF3_Pointer"""
    return _itkFrequencyShrinkViaInverseFFTImageFilterPython.itkFrequencyShrinkViaInverseFFTImageFilterICF3___New_orig__()

def itkFrequencyShrinkViaInverseFFTImageFilterICF3_cast(obj: 'itkLightObject') -> "itkFrequencyShrinkViaInverseFFTImageFilterICF3 *":
    """itkFrequencyShrinkViaInverseFFTImageFilterICF3_cast(itkLightObject obj) -> itkFrequencyShrinkViaInverseFFTImageFilterICF3"""
    return _itkFrequencyShrinkViaInverseFFTImageFilterPython.itkFrequencyShrinkViaInverseFFTImageFilterICF3_cast(obj)


def frequency_shrink_via_inverse_fft_image_filter(*args, **kwargs):
    """Procedural interface for FrequencyShrinkViaInverseFFTImageFilter"""
    import itk
    return itk.FrequencyShrinkViaInverseFFTImageFilter.__call__(*args, **kwargs)



