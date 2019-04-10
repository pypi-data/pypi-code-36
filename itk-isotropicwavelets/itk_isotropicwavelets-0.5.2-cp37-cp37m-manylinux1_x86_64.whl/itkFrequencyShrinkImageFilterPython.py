# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.8
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkFrequencyShrinkImageFilterPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkFrequencyShrinkImageFilterPython', [dirname(__file__)])
        except ImportError:
            import _itkFrequencyShrinkImageFilterPython
            return _itkFrequencyShrinkImageFilterPython
        if fp is not None:
            try:
                _mod = imp.load_module('_itkFrequencyShrinkImageFilterPython', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _itkFrequencyShrinkImageFilterPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkFrequencyShrinkImageFilterPython
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


import itkFixedArrayPython
import pyBasePython
import itkImageToImageFilterBPython
import itkImageRegionPython
import ITKCommonBasePython
import itkIndexPython
import itkOffsetPython
import itkSizePython
import itkImageToImageFilterCommonPython
import itkImagePython
import itkMatrixPython
import itkCovariantVectorPython
import vnl_vector_refPython
import stdcomplexPython
import vnl_vectorPython
import vnl_matrixPython
import itkVectorPython
import vnl_matrix_fixedPython
import itkPointPython
import itkRGBAPixelPython
import itkRGBPixelPython
import itkSymmetricSecondRankTensorPython
import itkVectorImagePython
import itkVariableLengthVectorPython
import itkImageSourcePython
import itkImageSourceCommonPython
import itkFrequencyBandImageFilterPython
import itkUnaryFrequencyDomainFilterPython
import itkInPlaceImageFilterBPython

def itkFrequencyShrinkImageFilterICF3_New():
  return itkFrequencyShrinkImageFilterICF3.New()


def itkFrequencyShrinkImageFilterICF2_New():
  return itkFrequencyShrinkImageFilterICF2.New()

class itkFrequencyShrinkImageFilterICF2(itkImageToImageFilterBPython.itkImageToImageFilterICF2ICF2):
    """Proxy of C++ itkFrequencyShrinkImageFilterICF2 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkFrequencyShrinkImageFilterICF2_Pointer":
        """__New_orig__() -> itkFrequencyShrinkImageFilterICF2_Pointer"""
        return _itkFrequencyShrinkImageFilterPython.itkFrequencyShrinkImageFilterICF2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkFrequencyShrinkImageFilterICF2_Pointer":
        """Clone(itkFrequencyShrinkImageFilterICF2 self) -> itkFrequencyShrinkImageFilterICF2_Pointer"""
        return _itkFrequencyShrinkImageFilterPython.itkFrequencyShrinkImageFilterICF2_Clone(self)


    def SetShrinkFactors(self, *args) -> "void":
        """
        SetShrinkFactors(itkFrequencyShrinkImageFilterICF2 self, itkFixedArrayUI2 _arg)
        SetShrinkFactors(itkFrequencyShrinkImageFilterICF2 self, unsigned int factor)
        """
        return _itkFrequencyShrinkImageFilterPython.itkFrequencyShrinkImageFilterICF2_SetShrinkFactors(self, *args)


    def SetShrinkFactor(self, i: 'unsigned int', factor: 'unsigned int') -> "void":
        """SetShrinkFactor(itkFrequencyShrinkImageFilterICF2 self, unsigned int i, unsigned int factor)"""
        return _itkFrequencyShrinkImageFilterPython.itkFrequencyShrinkImageFilterICF2_SetShrinkFactor(self, i, factor)


    def GetShrinkFactors(self) -> "itkFixedArrayUI2 const &":
        """GetShrinkFactors(itkFrequencyShrinkImageFilterICF2 self) -> itkFixedArrayUI2"""
        return _itkFrequencyShrinkImageFilterPython.itkFrequencyShrinkImageFilterICF2_GetShrinkFactors(self)


    def GenerateOutputInformation(self) -> "void":
        """GenerateOutputInformation(itkFrequencyShrinkImageFilterICF2 self)"""
        return _itkFrequencyShrinkImageFilterPython.itkFrequencyShrinkImageFilterICF2_GenerateOutputInformation(self)


    def GenerateInputRequestedRegion(self) -> "void":
        """GenerateInputRequestedRegion(itkFrequencyShrinkImageFilterICF2 self)"""
        return _itkFrequencyShrinkImageFilterPython.itkFrequencyShrinkImageFilterICF2_GenerateInputRequestedRegion(self)

    ImageTypeHasNumericTraitsCheck = _itkFrequencyShrinkImageFilterPython.itkFrequencyShrinkImageFilterICF2_ImageTypeHasNumericTraitsCheck

    def GetApplyBandFilter(self) -> "bool const &":
        """GetApplyBandFilter(itkFrequencyShrinkImageFilterICF2 self) -> bool const &"""
        return _itkFrequencyShrinkImageFilterPython.itkFrequencyShrinkImageFilterICF2_GetApplyBandFilter(self)


    def SetApplyBandFilter(self, _arg: 'bool const') -> "void":
        """SetApplyBandFilter(itkFrequencyShrinkImageFilterICF2 self, bool const _arg)"""
        return _itkFrequencyShrinkImageFilterPython.itkFrequencyShrinkImageFilterICF2_SetApplyBandFilter(self, _arg)


    def ApplyBandFilterOn(self) -> "void":
        """ApplyBandFilterOn(itkFrequencyShrinkImageFilterICF2 self)"""
        return _itkFrequencyShrinkImageFilterPython.itkFrequencyShrinkImageFilterICF2_ApplyBandFilterOn(self)


    def ApplyBandFilterOff(self) -> "void":
        """ApplyBandFilterOff(itkFrequencyShrinkImageFilterICF2 self)"""
        return _itkFrequencyShrinkImageFilterPython.itkFrequencyShrinkImageFilterICF2_ApplyBandFilterOff(self)


    def GetFrequencyBandFilter(self) -> "itkFrequencyBandImageFilterICF2_Pointer":
        """GetFrequencyBandFilter(itkFrequencyShrinkImageFilterICF2 self) -> itkFrequencyBandImageFilterICF2_Pointer"""
        return _itkFrequencyShrinkImageFilterPython.itkFrequencyShrinkImageFilterICF2_GetFrequencyBandFilter(self)

    __swig_destroy__ = _itkFrequencyShrinkImageFilterPython.delete_itkFrequencyShrinkImageFilterICF2

    def cast(obj: 'itkLightObject') -> "itkFrequencyShrinkImageFilterICF2 *":
        """cast(itkLightObject obj) -> itkFrequencyShrinkImageFilterICF2"""
        return _itkFrequencyShrinkImageFilterPython.itkFrequencyShrinkImageFilterICF2_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkFrequencyShrinkImageFilterICF2

        Create a new object of the class itkFrequencyShrinkImageFilterICF2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkFrequencyShrinkImageFilterICF2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkFrequencyShrinkImageFilterICF2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkFrequencyShrinkImageFilterICF2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkFrequencyShrinkImageFilterICF2.Clone = new_instancemethod(_itkFrequencyShrinkImageFilterPython.itkFrequencyShrinkImageFilterICF2_Clone, None, itkFrequencyShrinkImageFilterICF2)
itkFrequencyShrinkImageFilterICF2.SetShrinkFactors = new_instancemethod(_itkFrequencyShrinkImageFilterPython.itkFrequencyShrinkImageFilterICF2_SetShrinkFactors, None, itkFrequencyShrinkImageFilterICF2)
itkFrequencyShrinkImageFilterICF2.SetShrinkFactor = new_instancemethod(_itkFrequencyShrinkImageFilterPython.itkFrequencyShrinkImageFilterICF2_SetShrinkFactor, None, itkFrequencyShrinkImageFilterICF2)
itkFrequencyShrinkImageFilterICF2.GetShrinkFactors = new_instancemethod(_itkFrequencyShrinkImageFilterPython.itkFrequencyShrinkImageFilterICF2_GetShrinkFactors, None, itkFrequencyShrinkImageFilterICF2)
itkFrequencyShrinkImageFilterICF2.GenerateOutputInformation = new_instancemethod(_itkFrequencyShrinkImageFilterPython.itkFrequencyShrinkImageFilterICF2_GenerateOutputInformation, None, itkFrequencyShrinkImageFilterICF2)
itkFrequencyShrinkImageFilterICF2.GenerateInputRequestedRegion = new_instancemethod(_itkFrequencyShrinkImageFilterPython.itkFrequencyShrinkImageFilterICF2_GenerateInputRequestedRegion, None, itkFrequencyShrinkImageFilterICF2)
itkFrequencyShrinkImageFilterICF2.GetApplyBandFilter = new_instancemethod(_itkFrequencyShrinkImageFilterPython.itkFrequencyShrinkImageFilterICF2_GetApplyBandFilter, None, itkFrequencyShrinkImageFilterICF2)
itkFrequencyShrinkImageFilterICF2.SetApplyBandFilter = new_instancemethod(_itkFrequencyShrinkImageFilterPython.itkFrequencyShrinkImageFilterICF2_SetApplyBandFilter, None, itkFrequencyShrinkImageFilterICF2)
itkFrequencyShrinkImageFilterICF2.ApplyBandFilterOn = new_instancemethod(_itkFrequencyShrinkImageFilterPython.itkFrequencyShrinkImageFilterICF2_ApplyBandFilterOn, None, itkFrequencyShrinkImageFilterICF2)
itkFrequencyShrinkImageFilterICF2.ApplyBandFilterOff = new_instancemethod(_itkFrequencyShrinkImageFilterPython.itkFrequencyShrinkImageFilterICF2_ApplyBandFilterOff, None, itkFrequencyShrinkImageFilterICF2)
itkFrequencyShrinkImageFilterICF2.GetFrequencyBandFilter = new_instancemethod(_itkFrequencyShrinkImageFilterPython.itkFrequencyShrinkImageFilterICF2_GetFrequencyBandFilter, None, itkFrequencyShrinkImageFilterICF2)
itkFrequencyShrinkImageFilterICF2_swigregister = _itkFrequencyShrinkImageFilterPython.itkFrequencyShrinkImageFilterICF2_swigregister
itkFrequencyShrinkImageFilterICF2_swigregister(itkFrequencyShrinkImageFilterICF2)

def itkFrequencyShrinkImageFilterICF2___New_orig__() -> "itkFrequencyShrinkImageFilterICF2_Pointer":
    """itkFrequencyShrinkImageFilterICF2___New_orig__() -> itkFrequencyShrinkImageFilterICF2_Pointer"""
    return _itkFrequencyShrinkImageFilterPython.itkFrequencyShrinkImageFilterICF2___New_orig__()

def itkFrequencyShrinkImageFilterICF2_cast(obj: 'itkLightObject') -> "itkFrequencyShrinkImageFilterICF2 *":
    """itkFrequencyShrinkImageFilterICF2_cast(itkLightObject obj) -> itkFrequencyShrinkImageFilterICF2"""
    return _itkFrequencyShrinkImageFilterPython.itkFrequencyShrinkImageFilterICF2_cast(obj)

class itkFrequencyShrinkImageFilterICF3(itkImageToImageFilterBPython.itkImageToImageFilterICF3ICF3):
    """Proxy of C++ itkFrequencyShrinkImageFilterICF3 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkFrequencyShrinkImageFilterICF3_Pointer":
        """__New_orig__() -> itkFrequencyShrinkImageFilterICF3_Pointer"""
        return _itkFrequencyShrinkImageFilterPython.itkFrequencyShrinkImageFilterICF3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkFrequencyShrinkImageFilterICF3_Pointer":
        """Clone(itkFrequencyShrinkImageFilterICF3 self) -> itkFrequencyShrinkImageFilterICF3_Pointer"""
        return _itkFrequencyShrinkImageFilterPython.itkFrequencyShrinkImageFilterICF3_Clone(self)


    def SetShrinkFactors(self, *args) -> "void":
        """
        SetShrinkFactors(itkFrequencyShrinkImageFilterICF3 self, itkFixedArrayUI3 _arg)
        SetShrinkFactors(itkFrequencyShrinkImageFilterICF3 self, unsigned int factor)
        """
        return _itkFrequencyShrinkImageFilterPython.itkFrequencyShrinkImageFilterICF3_SetShrinkFactors(self, *args)


    def SetShrinkFactor(self, i: 'unsigned int', factor: 'unsigned int') -> "void":
        """SetShrinkFactor(itkFrequencyShrinkImageFilterICF3 self, unsigned int i, unsigned int factor)"""
        return _itkFrequencyShrinkImageFilterPython.itkFrequencyShrinkImageFilterICF3_SetShrinkFactor(self, i, factor)


    def GetShrinkFactors(self) -> "itkFixedArrayUI3 const &":
        """GetShrinkFactors(itkFrequencyShrinkImageFilterICF3 self) -> itkFixedArrayUI3"""
        return _itkFrequencyShrinkImageFilterPython.itkFrequencyShrinkImageFilterICF3_GetShrinkFactors(self)


    def GenerateOutputInformation(self) -> "void":
        """GenerateOutputInformation(itkFrequencyShrinkImageFilterICF3 self)"""
        return _itkFrequencyShrinkImageFilterPython.itkFrequencyShrinkImageFilterICF3_GenerateOutputInformation(self)


    def GenerateInputRequestedRegion(self) -> "void":
        """GenerateInputRequestedRegion(itkFrequencyShrinkImageFilterICF3 self)"""
        return _itkFrequencyShrinkImageFilterPython.itkFrequencyShrinkImageFilterICF3_GenerateInputRequestedRegion(self)

    ImageTypeHasNumericTraitsCheck = _itkFrequencyShrinkImageFilterPython.itkFrequencyShrinkImageFilterICF3_ImageTypeHasNumericTraitsCheck

    def GetApplyBandFilter(self) -> "bool const &":
        """GetApplyBandFilter(itkFrequencyShrinkImageFilterICF3 self) -> bool const &"""
        return _itkFrequencyShrinkImageFilterPython.itkFrequencyShrinkImageFilterICF3_GetApplyBandFilter(self)


    def SetApplyBandFilter(self, _arg: 'bool const') -> "void":
        """SetApplyBandFilter(itkFrequencyShrinkImageFilterICF3 self, bool const _arg)"""
        return _itkFrequencyShrinkImageFilterPython.itkFrequencyShrinkImageFilterICF3_SetApplyBandFilter(self, _arg)


    def ApplyBandFilterOn(self) -> "void":
        """ApplyBandFilterOn(itkFrequencyShrinkImageFilterICF3 self)"""
        return _itkFrequencyShrinkImageFilterPython.itkFrequencyShrinkImageFilterICF3_ApplyBandFilterOn(self)


    def ApplyBandFilterOff(self) -> "void":
        """ApplyBandFilterOff(itkFrequencyShrinkImageFilterICF3 self)"""
        return _itkFrequencyShrinkImageFilterPython.itkFrequencyShrinkImageFilterICF3_ApplyBandFilterOff(self)


    def GetFrequencyBandFilter(self) -> "itkFrequencyBandImageFilterICF3_Pointer":
        """GetFrequencyBandFilter(itkFrequencyShrinkImageFilterICF3 self) -> itkFrequencyBandImageFilterICF3_Pointer"""
        return _itkFrequencyShrinkImageFilterPython.itkFrequencyShrinkImageFilterICF3_GetFrequencyBandFilter(self)

    __swig_destroy__ = _itkFrequencyShrinkImageFilterPython.delete_itkFrequencyShrinkImageFilterICF3

    def cast(obj: 'itkLightObject') -> "itkFrequencyShrinkImageFilterICF3 *":
        """cast(itkLightObject obj) -> itkFrequencyShrinkImageFilterICF3"""
        return _itkFrequencyShrinkImageFilterPython.itkFrequencyShrinkImageFilterICF3_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkFrequencyShrinkImageFilterICF3

        Create a new object of the class itkFrequencyShrinkImageFilterICF3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkFrequencyShrinkImageFilterICF3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkFrequencyShrinkImageFilterICF3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkFrequencyShrinkImageFilterICF3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkFrequencyShrinkImageFilterICF3.Clone = new_instancemethod(_itkFrequencyShrinkImageFilterPython.itkFrequencyShrinkImageFilterICF3_Clone, None, itkFrequencyShrinkImageFilterICF3)
itkFrequencyShrinkImageFilterICF3.SetShrinkFactors = new_instancemethod(_itkFrequencyShrinkImageFilterPython.itkFrequencyShrinkImageFilterICF3_SetShrinkFactors, None, itkFrequencyShrinkImageFilterICF3)
itkFrequencyShrinkImageFilterICF3.SetShrinkFactor = new_instancemethod(_itkFrequencyShrinkImageFilterPython.itkFrequencyShrinkImageFilterICF3_SetShrinkFactor, None, itkFrequencyShrinkImageFilterICF3)
itkFrequencyShrinkImageFilterICF3.GetShrinkFactors = new_instancemethod(_itkFrequencyShrinkImageFilterPython.itkFrequencyShrinkImageFilterICF3_GetShrinkFactors, None, itkFrequencyShrinkImageFilterICF3)
itkFrequencyShrinkImageFilterICF3.GenerateOutputInformation = new_instancemethod(_itkFrequencyShrinkImageFilterPython.itkFrequencyShrinkImageFilterICF3_GenerateOutputInformation, None, itkFrequencyShrinkImageFilterICF3)
itkFrequencyShrinkImageFilterICF3.GenerateInputRequestedRegion = new_instancemethod(_itkFrequencyShrinkImageFilterPython.itkFrequencyShrinkImageFilterICF3_GenerateInputRequestedRegion, None, itkFrequencyShrinkImageFilterICF3)
itkFrequencyShrinkImageFilterICF3.GetApplyBandFilter = new_instancemethod(_itkFrequencyShrinkImageFilterPython.itkFrequencyShrinkImageFilterICF3_GetApplyBandFilter, None, itkFrequencyShrinkImageFilterICF3)
itkFrequencyShrinkImageFilterICF3.SetApplyBandFilter = new_instancemethod(_itkFrequencyShrinkImageFilterPython.itkFrequencyShrinkImageFilterICF3_SetApplyBandFilter, None, itkFrequencyShrinkImageFilterICF3)
itkFrequencyShrinkImageFilterICF3.ApplyBandFilterOn = new_instancemethod(_itkFrequencyShrinkImageFilterPython.itkFrequencyShrinkImageFilterICF3_ApplyBandFilterOn, None, itkFrequencyShrinkImageFilterICF3)
itkFrequencyShrinkImageFilterICF3.ApplyBandFilterOff = new_instancemethod(_itkFrequencyShrinkImageFilterPython.itkFrequencyShrinkImageFilterICF3_ApplyBandFilterOff, None, itkFrequencyShrinkImageFilterICF3)
itkFrequencyShrinkImageFilterICF3.GetFrequencyBandFilter = new_instancemethod(_itkFrequencyShrinkImageFilterPython.itkFrequencyShrinkImageFilterICF3_GetFrequencyBandFilter, None, itkFrequencyShrinkImageFilterICF3)
itkFrequencyShrinkImageFilterICF3_swigregister = _itkFrequencyShrinkImageFilterPython.itkFrequencyShrinkImageFilterICF3_swigregister
itkFrequencyShrinkImageFilterICF3_swigregister(itkFrequencyShrinkImageFilterICF3)

def itkFrequencyShrinkImageFilterICF3___New_orig__() -> "itkFrequencyShrinkImageFilterICF3_Pointer":
    """itkFrequencyShrinkImageFilterICF3___New_orig__() -> itkFrequencyShrinkImageFilterICF3_Pointer"""
    return _itkFrequencyShrinkImageFilterPython.itkFrequencyShrinkImageFilterICF3___New_orig__()

def itkFrequencyShrinkImageFilterICF3_cast(obj: 'itkLightObject') -> "itkFrequencyShrinkImageFilterICF3 *":
    """itkFrequencyShrinkImageFilterICF3_cast(itkLightObject obj) -> itkFrequencyShrinkImageFilterICF3"""
    return _itkFrequencyShrinkImageFilterPython.itkFrequencyShrinkImageFilterICF3_cast(obj)


def frequency_shrink_image_filter(*args, **kwargs):
    """Procedural interface for FrequencyShrinkImageFilter"""
    import itk
    return itk.FrequencyShrinkImageFilter.__call__(*args, **kwargs)



