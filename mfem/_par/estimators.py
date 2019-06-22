# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_estimators')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_estimators')
    _estimators = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_estimators', [dirname(__file__)])
        except ImportError:
            import _estimators
            return _estimators
        try:
            _mod = imp.load_module('_estimators', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _estimators = swig_import_helper()
    del swig_import_helper
else:
    import _estimators
del _swig_python_version_info

try:
    _swig_property = property
except NameError:
    pass  # Python < 2.2 doesn't have 'property'.

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

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
        if _newclass:
            object.__setattr__(self, name, value)
        else:
            self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)


def _swig_setattr(self, class_type, name, value):
    return _swig_setattr_nondynamic(self, class_type, name, value, 0)


def _swig_getattr(self, class_type, name):
    if (name == "thisown"):
        return self.this.own()
    method = class_type.__swig_getmethods__.get(name, None)
    if method:
        return method(self)
    raise AttributeError("'%s' object has no attribute '%s'" % (class_type.__name__, name))


def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except __builtin__.Exception:
    class _object:
        pass
    _newclass = 0

try:
    import weakref
    weakref_proxy = weakref.proxy
except __builtin__.Exception:
    weakref_proxy = lambda x: x


MFEM_VERSION = _estimators.MFEM_VERSION
MFEM_VERSION_STRING = _estimators.MFEM_VERSION_STRING
MFEM_VERSION_TYPE = _estimators.MFEM_VERSION_TYPE
MFEM_VERSION_TYPE_RELEASE = _estimators.MFEM_VERSION_TYPE_RELEASE
MFEM_VERSION_TYPE_DEVELOPMENT = _estimators.MFEM_VERSION_TYPE_DEVELOPMENT
MFEM_VERSION_MAJOR = _estimators.MFEM_VERSION_MAJOR
MFEM_VERSION_MINOR = _estimators.MFEM_VERSION_MINOR
MFEM_VERSION_PATCH = _estimators.MFEM_VERSION_PATCH
MFEM_SOURCE_DIR = _estimators.MFEM_SOURCE_DIR
MFEM_INSTALL_DIR = _estimators.MFEM_INSTALL_DIR
MFEM_TIMER_TYPE = _estimators.MFEM_TIMER_TYPE
MFEM_HYPRE_VERSION = _estimators.MFEM_HYPRE_VERSION
import mfem._par.array
import mfem._par.ostream_typemap
import mfem._par.mem_manager
import mfem._par.vector
import mfem._par.fespace
import mfem._par.coefficient
import mfem._par.matrix
import mfem._par.operators
import mfem._par.intrules
import mfem._par.sparsemat
import mfem._par.densemat
import mfem._par.eltrans
import mfem._par.fe
import mfem._par.geom
import mfem._par.mesh
import mfem._par.ncmesh
import mfem._par.element
import mfem._par.table
import mfem._par.hash
import mfem._par.vertex
import mfem._par.gridfunc
import mfem._par.bilininteg
import mfem._par.fe_coll
import mfem._par.lininteg
import mfem._par.linearform
import mfem._par.handle
import mfem._par.hypre
import mfem._par.bilinearform
class AbstractErrorEstimator(_object):
    """Proxy of C++ mfem::AbstractErrorEstimator class."""

    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, AbstractErrorEstimator, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, AbstractErrorEstimator, name)
    __repr__ = _swig_repr
    __swig_destroy__ = _estimators.delete_AbstractErrorEstimator
    __del__ = lambda self: None

    def __init__(self):
        """__init__(mfem::AbstractErrorEstimator self) -> AbstractErrorEstimator"""
        this = _estimators.new_AbstractErrorEstimator()
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
AbstractErrorEstimator_swigregister = _estimators.AbstractErrorEstimator_swigregister
AbstractErrorEstimator_swigregister(AbstractErrorEstimator)

class ErrorEstimator(AbstractErrorEstimator):
    """Proxy of C++ mfem::ErrorEstimator class."""

    __swig_setmethods__ = {}
    for _s in [AbstractErrorEstimator]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, ErrorEstimator, name, value)
    __swig_getmethods__ = {}
    for _s in [AbstractErrorEstimator]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, ErrorEstimator, name)

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr

    def GetLocalErrors(self):
        """GetLocalErrors(ErrorEstimator self) -> Vector"""
        return _estimators.ErrorEstimator_GetLocalErrors(self)


    def Reset(self):
        """Reset(ErrorEstimator self)"""
        return _estimators.ErrorEstimator_Reset(self)

    __swig_destroy__ = _estimators.delete_ErrorEstimator
    __del__ = lambda self: None
ErrorEstimator_swigregister = _estimators.ErrorEstimator_swigregister
ErrorEstimator_swigregister(ErrorEstimator)

class AnisotropicErrorEstimator(ErrorEstimator):
    """Proxy of C++ mfem::AnisotropicErrorEstimator class."""

    __swig_setmethods__ = {}
    for _s in [ErrorEstimator]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, AnisotropicErrorEstimator, name, value)
    __swig_getmethods__ = {}
    for _s in [ErrorEstimator]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, AnisotropicErrorEstimator, name)

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr

    def GetAnisotropicFlags(self):
        """GetAnisotropicFlags(AnisotropicErrorEstimator self) -> intArray"""
        return _estimators.AnisotropicErrorEstimator_GetAnisotropicFlags(self)

    __swig_destroy__ = _estimators.delete_AnisotropicErrorEstimator
    __del__ = lambda self: None
AnisotropicErrorEstimator_swigregister = _estimators.AnisotropicErrorEstimator_swigregister
AnisotropicErrorEstimator_swigregister(AnisotropicErrorEstimator)

class ZienkiewiczZhuEstimator(AnisotropicErrorEstimator):
    """Proxy of C++ mfem::ZienkiewiczZhuEstimator class."""

    __swig_setmethods__ = {}
    for _s in [AnisotropicErrorEstimator]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, ZienkiewiczZhuEstimator, name, value)
    __swig_getmethods__ = {}
    for _s in [AnisotropicErrorEstimator]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, ZienkiewiczZhuEstimator, name)
    __repr__ = _swig_repr

    def SetAnisotropic(self, aniso=True):
        """
        SetAnisotropic(ZienkiewiczZhuEstimator self, bool aniso=True)
        SetAnisotropic(ZienkiewiczZhuEstimator self)
        """
        return _estimators.ZienkiewiczZhuEstimator_SetAnisotropic(self, aniso)


    def SetFluxAveraging(self, fa):
        """SetFluxAveraging(ZienkiewiczZhuEstimator self, int fa)"""
        return _estimators.ZienkiewiczZhuEstimator_SetFluxAveraging(self, fa)


    def GetTotalError(self):
        """GetTotalError(ZienkiewiczZhuEstimator self) -> double"""
        return _estimators.ZienkiewiczZhuEstimator_GetTotalError(self)


    def GetLocalErrors(self):
        """GetLocalErrors(ZienkiewiczZhuEstimator self) -> Vector"""
        return _estimators.ZienkiewiczZhuEstimator_GetLocalErrors(self)


    def GetAnisotropicFlags(self):
        """GetAnisotropicFlags(ZienkiewiczZhuEstimator self) -> intArray"""
        return _estimators.ZienkiewiczZhuEstimator_GetAnisotropicFlags(self)


    def Reset(self):
        """Reset(ZienkiewiczZhuEstimator self)"""
        return _estimators.ZienkiewiczZhuEstimator_Reset(self)

    __swig_destroy__ = _estimators.delete_ZienkiewiczZhuEstimator
    __del__ = lambda self: None

    def __init__(self, integ, sol, flux_fes, own_flux_fes=False):
        """
        __init__(mfem::ZienkiewiczZhuEstimator self, BilinearFormIntegrator integ, GridFunction sol, FiniteElementSpace flux_fes, bool own_flux_fes=False) -> ZienkiewiczZhuEstimator
        __init__(mfem::ZienkiewiczZhuEstimator self, BilinearFormIntegrator integ, GridFunction sol, FiniteElementSpace flux_fes) -> ZienkiewiczZhuEstimator
        """

        if own_flux_fes: flux_fes.thisown=0


        this = _estimators.new_ZienkiewiczZhuEstimator(integ, sol, flux_fes, own_flux_fes)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
ZienkiewiczZhuEstimator_swigregister = _estimators.ZienkiewiczZhuEstimator_swigregister
ZienkiewiczZhuEstimator_swigregister(ZienkiewiczZhuEstimator)

class L2ZienkiewiczZhuEstimator(ErrorEstimator):
    """Proxy of C++ mfem::L2ZienkiewiczZhuEstimator class."""

    __swig_setmethods__ = {}
    for _s in [ErrorEstimator]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, L2ZienkiewiczZhuEstimator, name, value)
    __swig_getmethods__ = {}
    for _s in [ErrorEstimator]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, L2ZienkiewiczZhuEstimator, name)
    __repr__ = _swig_repr

    def SetLocalErrorNormP(self, p):
        """SetLocalErrorNormP(L2ZienkiewiczZhuEstimator self, int p)"""
        return _estimators.L2ZienkiewiczZhuEstimator_SetLocalErrorNormP(self, p)


    def GetTotalError(self):
        """GetTotalError(L2ZienkiewiczZhuEstimator self) -> double"""
        return _estimators.L2ZienkiewiczZhuEstimator_GetTotalError(self)


    def GetLocalErrors(self):
        """GetLocalErrors(L2ZienkiewiczZhuEstimator self) -> Vector"""
        return _estimators.L2ZienkiewiczZhuEstimator_GetLocalErrors(self)


    def Reset(self):
        """Reset(L2ZienkiewiczZhuEstimator self)"""
        return _estimators.L2ZienkiewiczZhuEstimator_Reset(self)

    __swig_destroy__ = _estimators.delete_L2ZienkiewiczZhuEstimator
    __del__ = lambda self: None

    def __init__(self, integ, sol, flux_fes, smooth_flux_fes, own_flux_fes=False):
        """
        __init__(mfem::L2ZienkiewiczZhuEstimator self, BilinearFormIntegrator integ, mfem::ParGridFunction & sol, mfem::ParFiniteElementSpace * flux_fes, mfem::ParFiniteElementSpace * smooth_flux_fes, bool own_flux_fes=False) -> L2ZienkiewiczZhuEstimator
        __init__(mfem::L2ZienkiewiczZhuEstimator self, BilinearFormIntegrator integ, mfem::ParGridFunction & sol, mfem::ParFiniteElementSpace * flux_fes, mfem::ParFiniteElementSpace * smooth_flux_fes) -> L2ZienkiewiczZhuEstimator
        """

        if own_flux_fes: flux_fes.thisown=0


        this = _estimators.new_L2ZienkiewiczZhuEstimator(integ, sol, flux_fes, smooth_flux_fes, own_flux_fes)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
L2ZienkiewiczZhuEstimator_swigregister = _estimators.L2ZienkiewiczZhuEstimator_swigregister
L2ZienkiewiczZhuEstimator_swigregister(L2ZienkiewiczZhuEstimator)

# This file is compatible with both classic and new-style classes.


