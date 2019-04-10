# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.8
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkMonogenicSignalFrequencyImageFilterPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkMonogenicSignalFrequencyImageFilterPython', [dirname(__file__)])
        except ImportError:
            import _itkMonogenicSignalFrequencyImageFilterPython
            return _itkMonogenicSignalFrequencyImageFilterPython
        if fp is not None:
            try:
                _mod = imp.load_module('_itkMonogenicSignalFrequencyImageFilterPython', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _itkMonogenicSignalFrequencyImageFilterPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkMonogenicSignalFrequencyImageFilterPython
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


import itkImageToImageFilterCommonPython
import pyBasePython
import itkImageRegionPython
import ITKCommonBasePython
import itkIndexPython
import itkOffsetPython
import itkSizePython
import itkImagePython
import itkMatrixPython
import itkCovariantVectorPython
import vnl_vector_refPython
import stdcomplexPython
import vnl_vectorPython
import vnl_matrixPython
import itkFixedArrayPython
import itkVectorPython
import vnl_matrix_fixedPython
import itkPointPython
import itkRGBAPixelPython
import itkRGBPixelPython
import itkSymmetricSecondRankTensorPython
import itkImageSourceCommonPython
import itkVectorImagePython
import itkVariableLengthVectorPython

def itkMonogenicSignalFrequencyImageFilterICF3_New():
  return itkMonogenicSignalFrequencyImageFilterICF3.New()


def itkMonogenicSignalFrequencyImageFilterICF2_New():
  return itkMonogenicSignalFrequencyImageFilterICF2.New()


def itkImageToImageFilterICF3VICF3_New():
  return itkImageToImageFilterICF3VICF3.New()


def itkImageToImageFilterICF2VICF2_New():
  return itkImageToImageFilterICF2VICF2.New()


def itkImageSourceVICF3_New():
  return itkImageSourceVICF3.New()


def itkImageSourceVICF2_New():
  return itkImageSourceVICF2.New()

class itkImageSourceVICF2(ITKCommonBasePython.itkProcessObject):
    """Proxy of C++ itkImageSourceVICF2 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def GetOutput(self, *args) -> "itkVectorImageCF2 *":
        """
        GetOutput(itkImageSourceVICF2 self) -> itkVectorImageCF2
        GetOutput(itkImageSourceVICF2 self) -> itkVectorImageCF2
        GetOutput(itkImageSourceVICF2 self, unsigned int idx) -> itkVectorImageCF2
        """
        return _itkMonogenicSignalFrequencyImageFilterPython.itkImageSourceVICF2_GetOutput(self, *args)


    def GraftOutput(self, *args) -> "void":
        """
        GraftOutput(itkImageSourceVICF2 self, itkDataObject output)
        GraftOutput(itkImageSourceVICF2 self, std::string const & key, itkDataObject output)
        """
        return _itkMonogenicSignalFrequencyImageFilterPython.itkImageSourceVICF2_GraftOutput(self, *args)


    def GraftNthOutput(self, idx: 'unsigned int', output: 'itkDataObject') -> "void":
        """GraftNthOutput(itkImageSourceVICF2 self, unsigned int idx, itkDataObject output)"""
        return _itkMonogenicSignalFrequencyImageFilterPython.itkImageSourceVICF2_GraftNthOutput(self, idx, output)


    def MakeOutput(self, *args) -> "itkDataObject_Pointer":
        """
        MakeOutput(itkImageSourceVICF2 self, unsigned long idx) -> itkDataObject_Pointer
        MakeOutput(itkImageSourceVICF2 self, std::string const & arg0) -> itkDataObject_Pointer

        Make a DataObject of the
        correct type to used as the specified output.

        Every ProcessObject subclass must be able to create a DataObject that
        can be used as a specified output. This method is automatically called
        when DataObject::DisconnectPipeline() is called.
        DataObject::DisconnectPipeline, disconnects a data object from being
        an output of its current source. When the data object is disconnected,
        the ProcessObject needs to construct a replacement output data object
        so that the ProcessObject is in a valid state. So
        DataObject::DisconnectPipeline eventually calls
        ProcessObject::MakeOutput. Note that MakeOutput always returns a
        itkSmartPointer to a DataObject. ImageSource and MeshSource override
        this method to create the correct type of image and mesh respectively.
        If a filter has multiple outputs of different types, then that filter
        must provide an implementation of MakeOutput(). 
        """
        return _itkMonogenicSignalFrequencyImageFilterPython.itkImageSourceVICF2_MakeOutput(self, *args)

    __swig_destroy__ = _itkMonogenicSignalFrequencyImageFilterPython.delete_itkImageSourceVICF2

    def cast(obj: 'itkLightObject') -> "itkImageSourceVICF2 *":
        """cast(itkLightObject obj) -> itkImageSourceVICF2"""
        return _itkMonogenicSignalFrequencyImageFilterPython.itkImageSourceVICF2_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkImageSourceVICF2

        Create a new object of the class itkImageSourceVICF2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkImageSourceVICF2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkImageSourceVICF2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkImageSourceVICF2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkImageSourceVICF2.GetOutput = new_instancemethod(_itkMonogenicSignalFrequencyImageFilterPython.itkImageSourceVICF2_GetOutput, None, itkImageSourceVICF2)
itkImageSourceVICF2.GraftOutput = new_instancemethod(_itkMonogenicSignalFrequencyImageFilterPython.itkImageSourceVICF2_GraftOutput, None, itkImageSourceVICF2)
itkImageSourceVICF2.GraftNthOutput = new_instancemethod(_itkMonogenicSignalFrequencyImageFilterPython.itkImageSourceVICF2_GraftNthOutput, None, itkImageSourceVICF2)
itkImageSourceVICF2.MakeOutput = new_instancemethod(_itkMonogenicSignalFrequencyImageFilterPython.itkImageSourceVICF2_MakeOutput, None, itkImageSourceVICF2)
itkImageSourceVICF2_swigregister = _itkMonogenicSignalFrequencyImageFilterPython.itkImageSourceVICF2_swigregister
itkImageSourceVICF2_swigregister(itkImageSourceVICF2)

def itkImageSourceVICF2_cast(obj: 'itkLightObject') -> "itkImageSourceVICF2 *":
    """itkImageSourceVICF2_cast(itkLightObject obj) -> itkImageSourceVICF2"""
    return _itkMonogenicSignalFrequencyImageFilterPython.itkImageSourceVICF2_cast(obj)

class itkImageSourceVICF3(ITKCommonBasePython.itkProcessObject):
    """Proxy of C++ itkImageSourceVICF3 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def GetOutput(self, *args) -> "itkVectorImageCF3 *":
        """
        GetOutput(itkImageSourceVICF3 self) -> itkVectorImageCF3
        GetOutput(itkImageSourceVICF3 self) -> itkVectorImageCF3
        GetOutput(itkImageSourceVICF3 self, unsigned int idx) -> itkVectorImageCF3
        """
        return _itkMonogenicSignalFrequencyImageFilterPython.itkImageSourceVICF3_GetOutput(self, *args)


    def GraftOutput(self, *args) -> "void":
        """
        GraftOutput(itkImageSourceVICF3 self, itkDataObject output)
        GraftOutput(itkImageSourceVICF3 self, std::string const & key, itkDataObject output)
        """
        return _itkMonogenicSignalFrequencyImageFilterPython.itkImageSourceVICF3_GraftOutput(self, *args)


    def GraftNthOutput(self, idx: 'unsigned int', output: 'itkDataObject') -> "void":
        """GraftNthOutput(itkImageSourceVICF3 self, unsigned int idx, itkDataObject output)"""
        return _itkMonogenicSignalFrequencyImageFilterPython.itkImageSourceVICF3_GraftNthOutput(self, idx, output)


    def MakeOutput(self, *args) -> "itkDataObject_Pointer":
        """
        MakeOutput(itkImageSourceVICF3 self, unsigned long idx) -> itkDataObject_Pointer
        MakeOutput(itkImageSourceVICF3 self, std::string const & arg0) -> itkDataObject_Pointer

        Make a DataObject of the
        correct type to used as the specified output.

        Every ProcessObject subclass must be able to create a DataObject that
        can be used as a specified output. This method is automatically called
        when DataObject::DisconnectPipeline() is called.
        DataObject::DisconnectPipeline, disconnects a data object from being
        an output of its current source. When the data object is disconnected,
        the ProcessObject needs to construct a replacement output data object
        so that the ProcessObject is in a valid state. So
        DataObject::DisconnectPipeline eventually calls
        ProcessObject::MakeOutput. Note that MakeOutput always returns a
        itkSmartPointer to a DataObject. ImageSource and MeshSource override
        this method to create the correct type of image and mesh respectively.
        If a filter has multiple outputs of different types, then that filter
        must provide an implementation of MakeOutput(). 
        """
        return _itkMonogenicSignalFrequencyImageFilterPython.itkImageSourceVICF3_MakeOutput(self, *args)

    __swig_destroy__ = _itkMonogenicSignalFrequencyImageFilterPython.delete_itkImageSourceVICF3

    def cast(obj: 'itkLightObject') -> "itkImageSourceVICF3 *":
        """cast(itkLightObject obj) -> itkImageSourceVICF3"""
        return _itkMonogenicSignalFrequencyImageFilterPython.itkImageSourceVICF3_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkImageSourceVICF3

        Create a new object of the class itkImageSourceVICF3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkImageSourceVICF3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkImageSourceVICF3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkImageSourceVICF3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkImageSourceVICF3.GetOutput = new_instancemethod(_itkMonogenicSignalFrequencyImageFilterPython.itkImageSourceVICF3_GetOutput, None, itkImageSourceVICF3)
itkImageSourceVICF3.GraftOutput = new_instancemethod(_itkMonogenicSignalFrequencyImageFilterPython.itkImageSourceVICF3_GraftOutput, None, itkImageSourceVICF3)
itkImageSourceVICF3.GraftNthOutput = new_instancemethod(_itkMonogenicSignalFrequencyImageFilterPython.itkImageSourceVICF3_GraftNthOutput, None, itkImageSourceVICF3)
itkImageSourceVICF3.MakeOutput = new_instancemethod(_itkMonogenicSignalFrequencyImageFilterPython.itkImageSourceVICF3_MakeOutput, None, itkImageSourceVICF3)
itkImageSourceVICF3_swigregister = _itkMonogenicSignalFrequencyImageFilterPython.itkImageSourceVICF3_swigregister
itkImageSourceVICF3_swigregister(itkImageSourceVICF3)

def itkImageSourceVICF3_cast(obj: 'itkLightObject') -> "itkImageSourceVICF3 *":
    """itkImageSourceVICF3_cast(itkLightObject obj) -> itkImageSourceVICF3"""
    return _itkMonogenicSignalFrequencyImageFilterPython.itkImageSourceVICF3_cast(obj)

class itkImageToImageFilterICF2VICF2(itkImageSourceVICF2):
    """Proxy of C++ itkImageToImageFilterICF2VICF2 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def SetInput(self, *args) -> "void":
        """
        SetInput(itkImageToImageFilterICF2VICF2 self, itkImageCF2 image)
        SetInput(itkImageToImageFilterICF2VICF2 self, unsigned int arg0, itkImageCF2 image)
        """
        return _itkMonogenicSignalFrequencyImageFilterPython.itkImageToImageFilterICF2VICF2_SetInput(self, *args)


    def GetInput(self, *args) -> "itkImageCF2 const *":
        """
        GetInput(itkImageToImageFilterICF2VICF2 self) -> itkImageCF2
        GetInput(itkImageToImageFilterICF2VICF2 self, unsigned int idx) -> itkImageCF2
        """
        return _itkMonogenicSignalFrequencyImageFilterPython.itkImageToImageFilterICF2VICF2_GetInput(self, *args)


    def PushBackInput(self, image: 'itkImageCF2') -> "void":
        """PushBackInput(itkImageToImageFilterICF2VICF2 self, itkImageCF2 image)"""
        return _itkMonogenicSignalFrequencyImageFilterPython.itkImageToImageFilterICF2VICF2_PushBackInput(self, image)


    def PopBackInput(self) -> "void":
        """PopBackInput(itkImageToImageFilterICF2VICF2 self)"""
        return _itkMonogenicSignalFrequencyImageFilterPython.itkImageToImageFilterICF2VICF2_PopBackInput(self)


    def PushFrontInput(self, image: 'itkImageCF2') -> "void":
        """PushFrontInput(itkImageToImageFilterICF2VICF2 self, itkImageCF2 image)"""
        return _itkMonogenicSignalFrequencyImageFilterPython.itkImageToImageFilterICF2VICF2_PushFrontInput(self, image)


    def PopFrontInput(self) -> "void":
        """PopFrontInput(itkImageToImageFilterICF2VICF2 self)"""
        return _itkMonogenicSignalFrequencyImageFilterPython.itkImageToImageFilterICF2VICF2_PopFrontInput(self)


    def SetCoordinateTolerance(self, _arg: 'double const') -> "void":
        """SetCoordinateTolerance(itkImageToImageFilterICF2VICF2 self, double const _arg)"""
        return _itkMonogenicSignalFrequencyImageFilterPython.itkImageToImageFilterICF2VICF2_SetCoordinateTolerance(self, _arg)


    def GetCoordinateTolerance(self) -> "double":
        """GetCoordinateTolerance(itkImageToImageFilterICF2VICF2 self) -> double"""
        return _itkMonogenicSignalFrequencyImageFilterPython.itkImageToImageFilterICF2VICF2_GetCoordinateTolerance(self)


    def SetDirectionTolerance(self, _arg: 'double const') -> "void":
        """SetDirectionTolerance(itkImageToImageFilterICF2VICF2 self, double const _arg)"""
        return _itkMonogenicSignalFrequencyImageFilterPython.itkImageToImageFilterICF2VICF2_SetDirectionTolerance(self, _arg)


    def GetDirectionTolerance(self) -> "double":
        """GetDirectionTolerance(itkImageToImageFilterICF2VICF2 self) -> double"""
        return _itkMonogenicSignalFrequencyImageFilterPython.itkImageToImageFilterICF2VICF2_GetDirectionTolerance(self)

    __swig_destroy__ = _itkMonogenicSignalFrequencyImageFilterPython.delete_itkImageToImageFilterICF2VICF2

    def cast(obj: 'itkLightObject') -> "itkImageToImageFilterICF2VICF2 *":
        """cast(itkLightObject obj) -> itkImageToImageFilterICF2VICF2"""
        return _itkMonogenicSignalFrequencyImageFilterPython.itkImageToImageFilterICF2VICF2_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkImageToImageFilterICF2VICF2

        Create a new object of the class itkImageToImageFilterICF2VICF2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkImageToImageFilterICF2VICF2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkImageToImageFilterICF2VICF2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkImageToImageFilterICF2VICF2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkImageToImageFilterICF2VICF2.SetInput = new_instancemethod(_itkMonogenicSignalFrequencyImageFilterPython.itkImageToImageFilterICF2VICF2_SetInput, None, itkImageToImageFilterICF2VICF2)
itkImageToImageFilterICF2VICF2.GetInput = new_instancemethod(_itkMonogenicSignalFrequencyImageFilterPython.itkImageToImageFilterICF2VICF2_GetInput, None, itkImageToImageFilterICF2VICF2)
itkImageToImageFilterICF2VICF2.PushBackInput = new_instancemethod(_itkMonogenicSignalFrequencyImageFilterPython.itkImageToImageFilterICF2VICF2_PushBackInput, None, itkImageToImageFilterICF2VICF2)
itkImageToImageFilterICF2VICF2.PopBackInput = new_instancemethod(_itkMonogenicSignalFrequencyImageFilterPython.itkImageToImageFilterICF2VICF2_PopBackInput, None, itkImageToImageFilterICF2VICF2)
itkImageToImageFilterICF2VICF2.PushFrontInput = new_instancemethod(_itkMonogenicSignalFrequencyImageFilterPython.itkImageToImageFilterICF2VICF2_PushFrontInput, None, itkImageToImageFilterICF2VICF2)
itkImageToImageFilterICF2VICF2.PopFrontInput = new_instancemethod(_itkMonogenicSignalFrequencyImageFilterPython.itkImageToImageFilterICF2VICF2_PopFrontInput, None, itkImageToImageFilterICF2VICF2)
itkImageToImageFilterICF2VICF2.SetCoordinateTolerance = new_instancemethod(_itkMonogenicSignalFrequencyImageFilterPython.itkImageToImageFilterICF2VICF2_SetCoordinateTolerance, None, itkImageToImageFilterICF2VICF2)
itkImageToImageFilterICF2VICF2.GetCoordinateTolerance = new_instancemethod(_itkMonogenicSignalFrequencyImageFilterPython.itkImageToImageFilterICF2VICF2_GetCoordinateTolerance, None, itkImageToImageFilterICF2VICF2)
itkImageToImageFilterICF2VICF2.SetDirectionTolerance = new_instancemethod(_itkMonogenicSignalFrequencyImageFilterPython.itkImageToImageFilterICF2VICF2_SetDirectionTolerance, None, itkImageToImageFilterICF2VICF2)
itkImageToImageFilterICF2VICF2.GetDirectionTolerance = new_instancemethod(_itkMonogenicSignalFrequencyImageFilterPython.itkImageToImageFilterICF2VICF2_GetDirectionTolerance, None, itkImageToImageFilterICF2VICF2)
itkImageToImageFilterICF2VICF2_swigregister = _itkMonogenicSignalFrequencyImageFilterPython.itkImageToImageFilterICF2VICF2_swigregister
itkImageToImageFilterICF2VICF2_swigregister(itkImageToImageFilterICF2VICF2)

def itkImageToImageFilterICF2VICF2_cast(obj: 'itkLightObject') -> "itkImageToImageFilterICF2VICF2 *":
    """itkImageToImageFilterICF2VICF2_cast(itkLightObject obj) -> itkImageToImageFilterICF2VICF2"""
    return _itkMonogenicSignalFrequencyImageFilterPython.itkImageToImageFilterICF2VICF2_cast(obj)

class itkImageToImageFilterICF3VICF3(itkImageSourceVICF3):
    """Proxy of C++ itkImageToImageFilterICF3VICF3 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def SetInput(self, *args) -> "void":
        """
        SetInput(itkImageToImageFilterICF3VICF3 self, itkImageCF3 image)
        SetInput(itkImageToImageFilterICF3VICF3 self, unsigned int arg0, itkImageCF3 image)
        """
        return _itkMonogenicSignalFrequencyImageFilterPython.itkImageToImageFilterICF3VICF3_SetInput(self, *args)


    def GetInput(self, *args) -> "itkImageCF3 const *":
        """
        GetInput(itkImageToImageFilterICF3VICF3 self) -> itkImageCF3
        GetInput(itkImageToImageFilterICF3VICF3 self, unsigned int idx) -> itkImageCF3
        """
        return _itkMonogenicSignalFrequencyImageFilterPython.itkImageToImageFilterICF3VICF3_GetInput(self, *args)


    def PushBackInput(self, image: 'itkImageCF3') -> "void":
        """PushBackInput(itkImageToImageFilterICF3VICF3 self, itkImageCF3 image)"""
        return _itkMonogenicSignalFrequencyImageFilterPython.itkImageToImageFilterICF3VICF3_PushBackInput(self, image)


    def PopBackInput(self) -> "void":
        """PopBackInput(itkImageToImageFilterICF3VICF3 self)"""
        return _itkMonogenicSignalFrequencyImageFilterPython.itkImageToImageFilterICF3VICF3_PopBackInput(self)


    def PushFrontInput(self, image: 'itkImageCF3') -> "void":
        """PushFrontInput(itkImageToImageFilterICF3VICF3 self, itkImageCF3 image)"""
        return _itkMonogenicSignalFrequencyImageFilterPython.itkImageToImageFilterICF3VICF3_PushFrontInput(self, image)


    def PopFrontInput(self) -> "void":
        """PopFrontInput(itkImageToImageFilterICF3VICF3 self)"""
        return _itkMonogenicSignalFrequencyImageFilterPython.itkImageToImageFilterICF3VICF3_PopFrontInput(self)


    def SetCoordinateTolerance(self, _arg: 'double const') -> "void":
        """SetCoordinateTolerance(itkImageToImageFilterICF3VICF3 self, double const _arg)"""
        return _itkMonogenicSignalFrequencyImageFilterPython.itkImageToImageFilterICF3VICF3_SetCoordinateTolerance(self, _arg)


    def GetCoordinateTolerance(self) -> "double":
        """GetCoordinateTolerance(itkImageToImageFilterICF3VICF3 self) -> double"""
        return _itkMonogenicSignalFrequencyImageFilterPython.itkImageToImageFilterICF3VICF3_GetCoordinateTolerance(self)


    def SetDirectionTolerance(self, _arg: 'double const') -> "void":
        """SetDirectionTolerance(itkImageToImageFilterICF3VICF3 self, double const _arg)"""
        return _itkMonogenicSignalFrequencyImageFilterPython.itkImageToImageFilterICF3VICF3_SetDirectionTolerance(self, _arg)


    def GetDirectionTolerance(self) -> "double":
        """GetDirectionTolerance(itkImageToImageFilterICF3VICF3 self) -> double"""
        return _itkMonogenicSignalFrequencyImageFilterPython.itkImageToImageFilterICF3VICF3_GetDirectionTolerance(self)

    __swig_destroy__ = _itkMonogenicSignalFrequencyImageFilterPython.delete_itkImageToImageFilterICF3VICF3

    def cast(obj: 'itkLightObject') -> "itkImageToImageFilterICF3VICF3 *":
        """cast(itkLightObject obj) -> itkImageToImageFilterICF3VICF3"""
        return _itkMonogenicSignalFrequencyImageFilterPython.itkImageToImageFilterICF3VICF3_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkImageToImageFilterICF3VICF3

        Create a new object of the class itkImageToImageFilterICF3VICF3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkImageToImageFilterICF3VICF3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkImageToImageFilterICF3VICF3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkImageToImageFilterICF3VICF3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkImageToImageFilterICF3VICF3.SetInput = new_instancemethod(_itkMonogenicSignalFrequencyImageFilterPython.itkImageToImageFilterICF3VICF3_SetInput, None, itkImageToImageFilterICF3VICF3)
itkImageToImageFilterICF3VICF3.GetInput = new_instancemethod(_itkMonogenicSignalFrequencyImageFilterPython.itkImageToImageFilterICF3VICF3_GetInput, None, itkImageToImageFilterICF3VICF3)
itkImageToImageFilterICF3VICF3.PushBackInput = new_instancemethod(_itkMonogenicSignalFrequencyImageFilterPython.itkImageToImageFilterICF3VICF3_PushBackInput, None, itkImageToImageFilterICF3VICF3)
itkImageToImageFilterICF3VICF3.PopBackInput = new_instancemethod(_itkMonogenicSignalFrequencyImageFilterPython.itkImageToImageFilterICF3VICF3_PopBackInput, None, itkImageToImageFilterICF3VICF3)
itkImageToImageFilterICF3VICF3.PushFrontInput = new_instancemethod(_itkMonogenicSignalFrequencyImageFilterPython.itkImageToImageFilterICF3VICF3_PushFrontInput, None, itkImageToImageFilterICF3VICF3)
itkImageToImageFilterICF3VICF3.PopFrontInput = new_instancemethod(_itkMonogenicSignalFrequencyImageFilterPython.itkImageToImageFilterICF3VICF3_PopFrontInput, None, itkImageToImageFilterICF3VICF3)
itkImageToImageFilterICF3VICF3.SetCoordinateTolerance = new_instancemethod(_itkMonogenicSignalFrequencyImageFilterPython.itkImageToImageFilterICF3VICF3_SetCoordinateTolerance, None, itkImageToImageFilterICF3VICF3)
itkImageToImageFilterICF3VICF3.GetCoordinateTolerance = new_instancemethod(_itkMonogenicSignalFrequencyImageFilterPython.itkImageToImageFilterICF3VICF3_GetCoordinateTolerance, None, itkImageToImageFilterICF3VICF3)
itkImageToImageFilterICF3VICF3.SetDirectionTolerance = new_instancemethod(_itkMonogenicSignalFrequencyImageFilterPython.itkImageToImageFilterICF3VICF3_SetDirectionTolerance, None, itkImageToImageFilterICF3VICF3)
itkImageToImageFilterICF3VICF3.GetDirectionTolerance = new_instancemethod(_itkMonogenicSignalFrequencyImageFilterPython.itkImageToImageFilterICF3VICF3_GetDirectionTolerance, None, itkImageToImageFilterICF3VICF3)
itkImageToImageFilterICF3VICF3_swigregister = _itkMonogenicSignalFrequencyImageFilterPython.itkImageToImageFilterICF3VICF3_swigregister
itkImageToImageFilterICF3VICF3_swigregister(itkImageToImageFilterICF3VICF3)

def itkImageToImageFilterICF3VICF3_cast(obj: 'itkLightObject') -> "itkImageToImageFilterICF3VICF3 *":
    """itkImageToImageFilterICF3VICF3_cast(itkLightObject obj) -> itkImageToImageFilterICF3VICF3"""
    return _itkMonogenicSignalFrequencyImageFilterPython.itkImageToImageFilterICF3VICF3_cast(obj)

class itkMonogenicSignalFrequencyImageFilterICF2(itkImageToImageFilterICF2VICF2):
    """Proxy of C++ itkMonogenicSignalFrequencyImageFilterICF2 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkMonogenicSignalFrequencyImageFilterICF2_Pointer":
        """__New_orig__() -> itkMonogenicSignalFrequencyImageFilterICF2_Pointer"""
        return _itkMonogenicSignalFrequencyImageFilterPython.itkMonogenicSignalFrequencyImageFilterICF2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkMonogenicSignalFrequencyImageFilterICF2_Pointer":
        """Clone(itkMonogenicSignalFrequencyImageFilterICF2 self) -> itkMonogenicSignalFrequencyImageFilterICF2_Pointer"""
        return _itkMonogenicSignalFrequencyImageFilterPython.itkMonogenicSignalFrequencyImageFilterICF2_Clone(self)

    InputPixelTypeIsComplexAndFloatCheck = _itkMonogenicSignalFrequencyImageFilterPython.itkMonogenicSignalFrequencyImageFilterICF2_InputPixelTypeIsComplexAndFloatCheck

    def GetModifiableEvaluator(self) -> "itk::RieszFrequencyFunction< std::complex< float >,2,itk::Point< double,2 > > *":
        """GetModifiableEvaluator(itkMonogenicSignalFrequencyImageFilterICF2 self) -> itk::RieszFrequencyFunction< std::complex< float >,2,itk::Point< double,2 > > *"""
        return _itkMonogenicSignalFrequencyImageFilterPython.itkMonogenicSignalFrequencyImageFilterICF2_GetModifiableEvaluator(self)


    def GetEvaluator(self, *args) -> "itk::RieszFrequencyFunction< std::complex< float >,2,itk::Point< double,2 > > *":
        """
        GetEvaluator(itkMonogenicSignalFrequencyImageFilterICF2 self) -> itk::RieszFrequencyFunction< std::complex< float >,2,itk::Point< double,2 > > const
        GetEvaluator(itkMonogenicSignalFrequencyImageFilterICF2 self) -> itk::RieszFrequencyFunction< std::complex< float >,2,itk::Point< double,2 > > *
        """
        return _itkMonogenicSignalFrequencyImageFilterPython.itkMonogenicSignalFrequencyImageFilterICF2_GetEvaluator(self, *args)

    __swig_destroy__ = _itkMonogenicSignalFrequencyImageFilterPython.delete_itkMonogenicSignalFrequencyImageFilterICF2

    def cast(obj: 'itkLightObject') -> "itkMonogenicSignalFrequencyImageFilterICF2 *":
        """cast(itkLightObject obj) -> itkMonogenicSignalFrequencyImageFilterICF2"""
        return _itkMonogenicSignalFrequencyImageFilterPython.itkMonogenicSignalFrequencyImageFilterICF2_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkMonogenicSignalFrequencyImageFilterICF2

        Create a new object of the class itkMonogenicSignalFrequencyImageFilterICF2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkMonogenicSignalFrequencyImageFilterICF2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkMonogenicSignalFrequencyImageFilterICF2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkMonogenicSignalFrequencyImageFilterICF2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkMonogenicSignalFrequencyImageFilterICF2.Clone = new_instancemethod(_itkMonogenicSignalFrequencyImageFilterPython.itkMonogenicSignalFrequencyImageFilterICF2_Clone, None, itkMonogenicSignalFrequencyImageFilterICF2)
itkMonogenicSignalFrequencyImageFilterICF2.GetModifiableEvaluator = new_instancemethod(_itkMonogenicSignalFrequencyImageFilterPython.itkMonogenicSignalFrequencyImageFilterICF2_GetModifiableEvaluator, None, itkMonogenicSignalFrequencyImageFilterICF2)
itkMonogenicSignalFrequencyImageFilterICF2.GetEvaluator = new_instancemethod(_itkMonogenicSignalFrequencyImageFilterPython.itkMonogenicSignalFrequencyImageFilterICF2_GetEvaluator, None, itkMonogenicSignalFrequencyImageFilterICF2)
itkMonogenicSignalFrequencyImageFilterICF2_swigregister = _itkMonogenicSignalFrequencyImageFilterPython.itkMonogenicSignalFrequencyImageFilterICF2_swigregister
itkMonogenicSignalFrequencyImageFilterICF2_swigregister(itkMonogenicSignalFrequencyImageFilterICF2)

def itkMonogenicSignalFrequencyImageFilterICF2___New_orig__() -> "itkMonogenicSignalFrequencyImageFilterICF2_Pointer":
    """itkMonogenicSignalFrequencyImageFilterICF2___New_orig__() -> itkMonogenicSignalFrequencyImageFilterICF2_Pointer"""
    return _itkMonogenicSignalFrequencyImageFilterPython.itkMonogenicSignalFrequencyImageFilterICF2___New_orig__()

def itkMonogenicSignalFrequencyImageFilterICF2_cast(obj: 'itkLightObject') -> "itkMonogenicSignalFrequencyImageFilterICF2 *":
    """itkMonogenicSignalFrequencyImageFilterICF2_cast(itkLightObject obj) -> itkMonogenicSignalFrequencyImageFilterICF2"""
    return _itkMonogenicSignalFrequencyImageFilterPython.itkMonogenicSignalFrequencyImageFilterICF2_cast(obj)

class itkMonogenicSignalFrequencyImageFilterICF3(itkImageToImageFilterICF3VICF3):
    """Proxy of C++ itkMonogenicSignalFrequencyImageFilterICF3 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkMonogenicSignalFrequencyImageFilterICF3_Pointer":
        """__New_orig__() -> itkMonogenicSignalFrequencyImageFilterICF3_Pointer"""
        return _itkMonogenicSignalFrequencyImageFilterPython.itkMonogenicSignalFrequencyImageFilterICF3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkMonogenicSignalFrequencyImageFilterICF3_Pointer":
        """Clone(itkMonogenicSignalFrequencyImageFilterICF3 self) -> itkMonogenicSignalFrequencyImageFilterICF3_Pointer"""
        return _itkMonogenicSignalFrequencyImageFilterPython.itkMonogenicSignalFrequencyImageFilterICF3_Clone(self)

    InputPixelTypeIsComplexAndFloatCheck = _itkMonogenicSignalFrequencyImageFilterPython.itkMonogenicSignalFrequencyImageFilterICF3_InputPixelTypeIsComplexAndFloatCheck

    def GetModifiableEvaluator(self) -> "itk::RieszFrequencyFunction< std::complex< float >,3,itk::Point< double,3 > > *":
        """GetModifiableEvaluator(itkMonogenicSignalFrequencyImageFilterICF3 self) -> itk::RieszFrequencyFunction< std::complex< float >,3,itk::Point< double,3 > > *"""
        return _itkMonogenicSignalFrequencyImageFilterPython.itkMonogenicSignalFrequencyImageFilterICF3_GetModifiableEvaluator(self)


    def GetEvaluator(self, *args) -> "itk::RieszFrequencyFunction< std::complex< float >,3,itk::Point< double,3 > > *":
        """
        GetEvaluator(itkMonogenicSignalFrequencyImageFilterICF3 self) -> itk::RieszFrequencyFunction< std::complex< float >,3,itk::Point< double,3 > > const
        GetEvaluator(itkMonogenicSignalFrequencyImageFilterICF3 self) -> itk::RieszFrequencyFunction< std::complex< float >,3,itk::Point< double,3 > > *
        """
        return _itkMonogenicSignalFrequencyImageFilterPython.itkMonogenicSignalFrequencyImageFilterICF3_GetEvaluator(self, *args)

    __swig_destroy__ = _itkMonogenicSignalFrequencyImageFilterPython.delete_itkMonogenicSignalFrequencyImageFilterICF3

    def cast(obj: 'itkLightObject') -> "itkMonogenicSignalFrequencyImageFilterICF3 *":
        """cast(itkLightObject obj) -> itkMonogenicSignalFrequencyImageFilterICF3"""
        return _itkMonogenicSignalFrequencyImageFilterPython.itkMonogenicSignalFrequencyImageFilterICF3_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkMonogenicSignalFrequencyImageFilterICF3

        Create a new object of the class itkMonogenicSignalFrequencyImageFilterICF3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkMonogenicSignalFrequencyImageFilterICF3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkMonogenicSignalFrequencyImageFilterICF3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkMonogenicSignalFrequencyImageFilterICF3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkMonogenicSignalFrequencyImageFilterICF3.Clone = new_instancemethod(_itkMonogenicSignalFrequencyImageFilterPython.itkMonogenicSignalFrequencyImageFilterICF3_Clone, None, itkMonogenicSignalFrequencyImageFilterICF3)
itkMonogenicSignalFrequencyImageFilterICF3.GetModifiableEvaluator = new_instancemethod(_itkMonogenicSignalFrequencyImageFilterPython.itkMonogenicSignalFrequencyImageFilterICF3_GetModifiableEvaluator, None, itkMonogenicSignalFrequencyImageFilterICF3)
itkMonogenicSignalFrequencyImageFilterICF3.GetEvaluator = new_instancemethod(_itkMonogenicSignalFrequencyImageFilterPython.itkMonogenicSignalFrequencyImageFilterICF3_GetEvaluator, None, itkMonogenicSignalFrequencyImageFilterICF3)
itkMonogenicSignalFrequencyImageFilterICF3_swigregister = _itkMonogenicSignalFrequencyImageFilterPython.itkMonogenicSignalFrequencyImageFilterICF3_swigregister
itkMonogenicSignalFrequencyImageFilterICF3_swigregister(itkMonogenicSignalFrequencyImageFilterICF3)

def itkMonogenicSignalFrequencyImageFilterICF3___New_orig__() -> "itkMonogenicSignalFrequencyImageFilterICF3_Pointer":
    """itkMonogenicSignalFrequencyImageFilterICF3___New_orig__() -> itkMonogenicSignalFrequencyImageFilterICF3_Pointer"""
    return _itkMonogenicSignalFrequencyImageFilterPython.itkMonogenicSignalFrequencyImageFilterICF3___New_orig__()

def itkMonogenicSignalFrequencyImageFilterICF3_cast(obj: 'itkLightObject') -> "itkMonogenicSignalFrequencyImageFilterICF3 *":
    """itkMonogenicSignalFrequencyImageFilterICF3_cast(itkLightObject obj) -> itkMonogenicSignalFrequencyImageFilterICF3"""
    return _itkMonogenicSignalFrequencyImageFilterPython.itkMonogenicSignalFrequencyImageFilterICF3_cast(obj)


def image_source(*args, **kwargs):
    """Procedural interface for ImageSource"""
    import itk
    return itk.ImageSource.__call__(*args, **kwargs)
def monogenic_signal_frequency_image_filter(*args, **kwargs):
    """Procedural interface for MonogenicSignalFrequencyImageFilter"""
    import itk
    return itk.MonogenicSignalFrequencyImageFilter.__call__(*args, **kwargs)
def image_to_image_filter(*args, **kwargs):
    """Procedural interface for ImageToImageFilter"""
    import itk
    return itk.ImageToImageFilter.__call__(*args, **kwargs)



