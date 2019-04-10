# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.8
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkRieszFrequencyFilterBankGeneratorPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkRieszFrequencyFilterBankGeneratorPython', [dirname(__file__)])
        except ImportError:
            import _itkRieszFrequencyFilterBankGeneratorPython
            return _itkRieszFrequencyFilterBankGeneratorPython
        if fp is not None:
            try:
                _mod = imp.load_module('_itkRieszFrequencyFilterBankGeneratorPython', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _itkRieszFrequencyFilterBankGeneratorPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkRieszFrequencyFilterBankGeneratorPython
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


import itkImageRegionPython
import itkIndexPython
import itkSizePython
import pyBasePython
import itkOffsetPython
import ITKCommonBasePython
import itkGenerateImageSourcePython
import itkImageSourcePython
import itkVectorImagePython
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
import itkMatrixPython
import vnl_matrix_fixedPython
import itkCovariantVectorPython
import itkSymmetricSecondRankTensorPython
import itkVariableLengthVectorPython
import itkImageSourceCommonPython

def itkRieszFrequencyFilterBankGeneratorICF3_New():
  return itkRieszFrequencyFilterBankGeneratorICF3.New()


def itkRieszFrequencyFilterBankGeneratorICF2_New():
  return itkRieszFrequencyFilterBankGeneratorICF2.New()

class itkRieszFrequencyFilterBankGeneratorICF2(itkGenerateImageSourcePython.itkGenerateImageSourceICF2):
    """Proxy of C++ itkRieszFrequencyFilterBankGeneratorICF2 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkRieszFrequencyFilterBankGeneratorICF2_Pointer":
        """__New_orig__() -> itkRieszFrequencyFilterBankGeneratorICF2_Pointer"""
        return _itkRieszFrequencyFilterBankGeneratorPython.itkRieszFrequencyFilterBankGeneratorICF2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkRieszFrequencyFilterBankGeneratorICF2_Pointer":
        """Clone(itkRieszFrequencyFilterBankGeneratorICF2 self) -> itkRieszFrequencyFilterBankGeneratorICF2_Pointer"""
        return _itkRieszFrequencyFilterBankGeneratorPython.itkRieszFrequencyFilterBankGeneratorICF2_Clone(self)


    def GetOutputs(self) -> "std::vector< itkImageCF2_Pointer,std::allocator< itkImageCF2_Pointer > >":
        """GetOutputs(itkRieszFrequencyFilterBankGeneratorICF2 self) -> std::vector< itkImageCF2_Pointer,std::allocator< itkImageCF2_Pointer > >"""
        return _itkRieszFrequencyFilterBankGeneratorPython.itkRieszFrequencyFilterBankGeneratorICF2_GetOutputs(self)


    def SetOrder(self, inputOrder: 'unsigned int const') -> "void":
        """SetOrder(itkRieszFrequencyFilterBankGeneratorICF2 self, unsigned int const inputOrder)"""
        return _itkRieszFrequencyFilterBankGeneratorPython.itkRieszFrequencyFilterBankGeneratorICF2_SetOrder(self, inputOrder)


    def GetOrder(self) -> "unsigned int const &":
        """GetOrder(itkRieszFrequencyFilterBankGeneratorICF2 self) -> unsigned int const &"""
        return _itkRieszFrequencyFilterBankGeneratorPython.itkRieszFrequencyFilterBankGeneratorICF2_GetOrder(self)


    def GetModifiableEvaluator(self) -> "itk::RieszFrequencyFunction< std::complex< double >,2,itk::Point< double,2 > > *":
        """GetModifiableEvaluator(itkRieszFrequencyFilterBankGeneratorICF2 self) -> itk::RieszFrequencyFunction< std::complex< double >,2,itk::Point< double,2 > > *"""
        return _itkRieszFrequencyFilterBankGeneratorPython.itkRieszFrequencyFilterBankGeneratorICF2_GetModifiableEvaluator(self)


    def GetEvaluator(self, *args) -> "itk::RieszFrequencyFunction< std::complex< double >,2,itk::Point< double,2 > > *":
        """
        GetEvaluator(itkRieszFrequencyFilterBankGeneratorICF2 self) -> itk::RieszFrequencyFunction< std::complex< double >,2,itk::Point< double,2 > > const
        GetEvaluator(itkRieszFrequencyFilterBankGeneratorICF2 self) -> itk::RieszFrequencyFunction< std::complex< double >,2,itk::Point< double,2 > > *
        """
        return _itkRieszFrequencyFilterBankGeneratorPython.itkRieszFrequencyFilterBankGeneratorICF2_GetEvaluator(self, *args)

    __swig_destroy__ = _itkRieszFrequencyFilterBankGeneratorPython.delete_itkRieszFrequencyFilterBankGeneratorICF2

    def cast(obj: 'itkLightObject') -> "itkRieszFrequencyFilterBankGeneratorICF2 *":
        """cast(itkLightObject obj) -> itkRieszFrequencyFilterBankGeneratorICF2"""
        return _itkRieszFrequencyFilterBankGeneratorPython.itkRieszFrequencyFilterBankGeneratorICF2_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkRieszFrequencyFilterBankGeneratorICF2

        Create a new object of the class itkRieszFrequencyFilterBankGeneratorICF2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkRieszFrequencyFilterBankGeneratorICF2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkRieszFrequencyFilterBankGeneratorICF2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkRieszFrequencyFilterBankGeneratorICF2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkRieszFrequencyFilterBankGeneratorICF2.Clone = new_instancemethod(_itkRieszFrequencyFilterBankGeneratorPython.itkRieszFrequencyFilterBankGeneratorICF2_Clone, None, itkRieszFrequencyFilterBankGeneratorICF2)
itkRieszFrequencyFilterBankGeneratorICF2.GetOutputs = new_instancemethod(_itkRieszFrequencyFilterBankGeneratorPython.itkRieszFrequencyFilterBankGeneratorICF2_GetOutputs, None, itkRieszFrequencyFilterBankGeneratorICF2)
itkRieszFrequencyFilterBankGeneratorICF2.SetOrder = new_instancemethod(_itkRieszFrequencyFilterBankGeneratorPython.itkRieszFrequencyFilterBankGeneratorICF2_SetOrder, None, itkRieszFrequencyFilterBankGeneratorICF2)
itkRieszFrequencyFilterBankGeneratorICF2.GetOrder = new_instancemethod(_itkRieszFrequencyFilterBankGeneratorPython.itkRieszFrequencyFilterBankGeneratorICF2_GetOrder, None, itkRieszFrequencyFilterBankGeneratorICF2)
itkRieszFrequencyFilterBankGeneratorICF2.GetModifiableEvaluator = new_instancemethod(_itkRieszFrequencyFilterBankGeneratorPython.itkRieszFrequencyFilterBankGeneratorICF2_GetModifiableEvaluator, None, itkRieszFrequencyFilterBankGeneratorICF2)
itkRieszFrequencyFilterBankGeneratorICF2.GetEvaluator = new_instancemethod(_itkRieszFrequencyFilterBankGeneratorPython.itkRieszFrequencyFilterBankGeneratorICF2_GetEvaluator, None, itkRieszFrequencyFilterBankGeneratorICF2)
itkRieszFrequencyFilterBankGeneratorICF2_swigregister = _itkRieszFrequencyFilterBankGeneratorPython.itkRieszFrequencyFilterBankGeneratorICF2_swigregister
itkRieszFrequencyFilterBankGeneratorICF2_swigregister(itkRieszFrequencyFilterBankGeneratorICF2)

def itkRieszFrequencyFilterBankGeneratorICF2___New_orig__() -> "itkRieszFrequencyFilterBankGeneratorICF2_Pointer":
    """itkRieszFrequencyFilterBankGeneratorICF2___New_orig__() -> itkRieszFrequencyFilterBankGeneratorICF2_Pointer"""
    return _itkRieszFrequencyFilterBankGeneratorPython.itkRieszFrequencyFilterBankGeneratorICF2___New_orig__()

def itkRieszFrequencyFilterBankGeneratorICF2_cast(obj: 'itkLightObject') -> "itkRieszFrequencyFilterBankGeneratorICF2 *":
    """itkRieszFrequencyFilterBankGeneratorICF2_cast(itkLightObject obj) -> itkRieszFrequencyFilterBankGeneratorICF2"""
    return _itkRieszFrequencyFilterBankGeneratorPython.itkRieszFrequencyFilterBankGeneratorICF2_cast(obj)

class itkRieszFrequencyFilterBankGeneratorICF3(itkGenerateImageSourcePython.itkGenerateImageSourceICF3):
    """Proxy of C++ itkRieszFrequencyFilterBankGeneratorICF3 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkRieszFrequencyFilterBankGeneratorICF3_Pointer":
        """__New_orig__() -> itkRieszFrequencyFilterBankGeneratorICF3_Pointer"""
        return _itkRieszFrequencyFilterBankGeneratorPython.itkRieszFrequencyFilterBankGeneratorICF3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkRieszFrequencyFilterBankGeneratorICF3_Pointer":
        """Clone(itkRieszFrequencyFilterBankGeneratorICF3 self) -> itkRieszFrequencyFilterBankGeneratorICF3_Pointer"""
        return _itkRieszFrequencyFilterBankGeneratorPython.itkRieszFrequencyFilterBankGeneratorICF3_Clone(self)


    def GetOutputs(self) -> "std::vector< itkImageCF3_Pointer,std::allocator< itkImageCF3_Pointer > >":
        """GetOutputs(itkRieszFrequencyFilterBankGeneratorICF3 self) -> std::vector< itkImageCF3_Pointer,std::allocator< itkImageCF3_Pointer > >"""
        return _itkRieszFrequencyFilterBankGeneratorPython.itkRieszFrequencyFilterBankGeneratorICF3_GetOutputs(self)


    def SetOrder(self, inputOrder: 'unsigned int const') -> "void":
        """SetOrder(itkRieszFrequencyFilterBankGeneratorICF3 self, unsigned int const inputOrder)"""
        return _itkRieszFrequencyFilterBankGeneratorPython.itkRieszFrequencyFilterBankGeneratorICF3_SetOrder(self, inputOrder)


    def GetOrder(self) -> "unsigned int const &":
        """GetOrder(itkRieszFrequencyFilterBankGeneratorICF3 self) -> unsigned int const &"""
        return _itkRieszFrequencyFilterBankGeneratorPython.itkRieszFrequencyFilterBankGeneratorICF3_GetOrder(self)


    def GetModifiableEvaluator(self) -> "itk::RieszFrequencyFunction< std::complex< double >,3,itk::Point< double,3 > > *":
        """GetModifiableEvaluator(itkRieszFrequencyFilterBankGeneratorICF3 self) -> itk::RieszFrequencyFunction< std::complex< double >,3,itk::Point< double,3 > > *"""
        return _itkRieszFrequencyFilterBankGeneratorPython.itkRieszFrequencyFilterBankGeneratorICF3_GetModifiableEvaluator(self)


    def GetEvaluator(self, *args) -> "itk::RieszFrequencyFunction< std::complex< double >,3,itk::Point< double,3 > > *":
        """
        GetEvaluator(itkRieszFrequencyFilterBankGeneratorICF3 self) -> itk::RieszFrequencyFunction< std::complex< double >,3,itk::Point< double,3 > > const
        GetEvaluator(itkRieszFrequencyFilterBankGeneratorICF3 self) -> itk::RieszFrequencyFunction< std::complex< double >,3,itk::Point< double,3 > > *
        """
        return _itkRieszFrequencyFilterBankGeneratorPython.itkRieszFrequencyFilterBankGeneratorICF3_GetEvaluator(self, *args)

    __swig_destroy__ = _itkRieszFrequencyFilterBankGeneratorPython.delete_itkRieszFrequencyFilterBankGeneratorICF3

    def cast(obj: 'itkLightObject') -> "itkRieszFrequencyFilterBankGeneratorICF3 *":
        """cast(itkLightObject obj) -> itkRieszFrequencyFilterBankGeneratorICF3"""
        return _itkRieszFrequencyFilterBankGeneratorPython.itkRieszFrequencyFilterBankGeneratorICF3_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkRieszFrequencyFilterBankGeneratorICF3

        Create a new object of the class itkRieszFrequencyFilterBankGeneratorICF3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkRieszFrequencyFilterBankGeneratorICF3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkRieszFrequencyFilterBankGeneratorICF3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkRieszFrequencyFilterBankGeneratorICF3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkRieszFrequencyFilterBankGeneratorICF3.Clone = new_instancemethod(_itkRieszFrequencyFilterBankGeneratorPython.itkRieszFrequencyFilterBankGeneratorICF3_Clone, None, itkRieszFrequencyFilterBankGeneratorICF3)
itkRieszFrequencyFilterBankGeneratorICF3.GetOutputs = new_instancemethod(_itkRieszFrequencyFilterBankGeneratorPython.itkRieszFrequencyFilterBankGeneratorICF3_GetOutputs, None, itkRieszFrequencyFilterBankGeneratorICF3)
itkRieszFrequencyFilterBankGeneratorICF3.SetOrder = new_instancemethod(_itkRieszFrequencyFilterBankGeneratorPython.itkRieszFrequencyFilterBankGeneratorICF3_SetOrder, None, itkRieszFrequencyFilterBankGeneratorICF3)
itkRieszFrequencyFilterBankGeneratorICF3.GetOrder = new_instancemethod(_itkRieszFrequencyFilterBankGeneratorPython.itkRieszFrequencyFilterBankGeneratorICF3_GetOrder, None, itkRieszFrequencyFilterBankGeneratorICF3)
itkRieszFrequencyFilterBankGeneratorICF3.GetModifiableEvaluator = new_instancemethod(_itkRieszFrequencyFilterBankGeneratorPython.itkRieszFrequencyFilterBankGeneratorICF3_GetModifiableEvaluator, None, itkRieszFrequencyFilterBankGeneratorICF3)
itkRieszFrequencyFilterBankGeneratorICF3.GetEvaluator = new_instancemethod(_itkRieszFrequencyFilterBankGeneratorPython.itkRieszFrequencyFilterBankGeneratorICF3_GetEvaluator, None, itkRieszFrequencyFilterBankGeneratorICF3)
itkRieszFrequencyFilterBankGeneratorICF3_swigregister = _itkRieszFrequencyFilterBankGeneratorPython.itkRieszFrequencyFilterBankGeneratorICF3_swigregister
itkRieszFrequencyFilterBankGeneratorICF3_swigregister(itkRieszFrequencyFilterBankGeneratorICF3)

def itkRieszFrequencyFilterBankGeneratorICF3___New_orig__() -> "itkRieszFrequencyFilterBankGeneratorICF3_Pointer":
    """itkRieszFrequencyFilterBankGeneratorICF3___New_orig__() -> itkRieszFrequencyFilterBankGeneratorICF3_Pointer"""
    return _itkRieszFrequencyFilterBankGeneratorPython.itkRieszFrequencyFilterBankGeneratorICF3___New_orig__()

def itkRieszFrequencyFilterBankGeneratorICF3_cast(obj: 'itkLightObject') -> "itkRieszFrequencyFilterBankGeneratorICF3 *":
    """itkRieszFrequencyFilterBankGeneratorICF3_cast(itkLightObject obj) -> itkRieszFrequencyFilterBankGeneratorICF3"""
    return _itkRieszFrequencyFilterBankGeneratorPython.itkRieszFrequencyFilterBankGeneratorICF3_cast(obj)


def riesz_frequency_filter_bank_generator(*args, **kwargs):
    """Procedural interface for RieszFrequencyFilterBankGenerator"""
    import itk
    return itk.RieszFrequencyFilterBankGenerator.__call__(*args, **kwargs)



