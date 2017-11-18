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
        mname = '.'.join((pkg, '_bilinearform')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_bilinearform')
    _bilinearform = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_bilinearform', [dirname(__file__)])
        except ImportError:
            import _bilinearform
            return _bilinearform
        try:
            _mod = imp.load_module('_bilinearform', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _bilinearform = swig_import_helper()
    del swig_import_helper
else:
    import _bilinearform
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


import array
import ostream_typemap
import fespace
import vector
import coefficient
import matrix
import operators
import intrules
import sparsemat
import densemat
import eltrans
import fe
import mesh
import ncmesh
import element
import geom
import table
import vertex
import gridfunc
import bilininteg
import fe_coll
import lininteg
import linearform
class BilinearForm(matrix.Matrix):
    __swig_setmethods__ = {}
    for _s in [matrix.Matrix]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, BilinearForm, name, value)
    __swig_getmethods__ = {}
    for _s in [matrix.Matrix]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, BilinearForm, name)
    __repr__ = _swig_repr

    def __init__(self, *args):
        this = _bilinearform.new_BilinearForm(*args)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def Size(self):
        return _bilinearform.BilinearForm_Size(self)

    def EnableStaticCondensation(self):
        return _bilinearform.BilinearForm_EnableStaticCondensation(self)

    def StaticCondensationIsEnabled(self):
        return _bilinearform.BilinearForm_StaticCondensationIsEnabled(self)

    def SCFESpace(self):
        return _bilinearform.BilinearForm_SCFESpace(self)

    def EnableHybridization(self, constr_space, constr_integ, ess_tdof_list):
        val = _bilinearform.BilinearForm_EnableHybridization(self, constr_space, constr_integ, ess_tdof_list)

        constr_integ.thisown = 0


        return val


    def UsePrecomputedSparsity(self, ps=1):
        return _bilinearform.BilinearForm_UsePrecomputedSparsity(self, ps)

    def UseSparsity(self, *args):
        return _bilinearform.BilinearForm_UseSparsity(self, *args)

    def AllocateMatrix(self):
        return _bilinearform.BilinearForm_AllocateMatrix(self)

    def GetDBFI(self):
        return _bilinearform.BilinearForm_GetDBFI(self)

    def GetBBFI(self):
        return _bilinearform.BilinearForm_GetBBFI(self)

    def GetFBFI(self):
        return _bilinearform.BilinearForm_GetFBFI(self)

    def GetBFBFI(self):
        return _bilinearform.BilinearForm_GetBFBFI(self)

    def __call__(self, i, j):
        return _bilinearform.BilinearForm___call__(self, i, j)

    def Elem(self, *args):
        return _bilinearform.BilinearForm_Elem(self, *args)

    def Mult(self, x, y):
        return _bilinearform.BilinearForm_Mult(self, x, y)

    def FullMult(self, x, y):
        return _bilinearform.BilinearForm_FullMult(self, x, y)

    def AddMult(self, x, y, a=1.0):
        return _bilinearform.BilinearForm_AddMult(self, x, y, a)

    def FullAddMult(self, x, y):
        return _bilinearform.BilinearForm_FullAddMult(self, x, y)

    def AddMultTranspose(self, x, y, a=1.0):
        return _bilinearform.BilinearForm_AddMultTranspose(self, x, y, a)

    def FullAddMultTranspose(self, x, y):
        return _bilinearform.BilinearForm_FullAddMultTranspose(self, x, y)

    def MultTranspose(self, x, y):
        return _bilinearform.BilinearForm_MultTranspose(self, x, y)

    def InnerProduct(self, x, y):
        return _bilinearform.BilinearForm_InnerProduct(self, x, y)

    def Inverse(self):
        return _bilinearform.BilinearForm_Inverse(self)

    def Finalize(self, skip_zeros=1):
        return _bilinearform.BilinearForm_Finalize(self, skip_zeros)

    def SpMat(self, *args):
        val = _bilinearform.BilinearForm_SpMat(self, *args)

        if not hasattr(self, "_spmat"): self._spmat = []
        self._spmat.append(val)
        val.thisown=0 


        return val


    def LoseMat(self):
        return _bilinearform.BilinearForm_LoseMat(self)

    def SpMatElim(self, *args):
        return _bilinearform.BilinearForm_SpMatElim(self, *args)

    def AddDomainIntegrator(self, bfi):

        if not hasattr(self, "_integrators"): self._integrators = []
        self._integrators.append(bfi)
        bfi.thisown=0 


        return _bilinearform.BilinearForm_AddDomainIntegrator(self, bfi)


    def AddBoundaryIntegrator(self, bfi):

        if not hasattr(self, "_integrators"): self._integrators = []
        self._integrators.append(bfi)
        bfi.thisown=0 


        return _bilinearform.BilinearForm_AddBoundaryIntegrator(self, bfi)


    def AddInteriorFaceIntegrator(self, bfi):

        if not hasattr(self, "_integrators"): self._integrators = []
        self._integrators.append(bfi)
        bfi.thisown=0 


        return _bilinearform.BilinearForm_AddInteriorFaceIntegrator(self, bfi)


    def AddBdrFaceIntegrator(self, *args):

        if not hasattr(self, "_integrators"): self._integrators = []
        bfi = args[0]	     
        self._integrators.append(bfi)
        bfi.thisown=0 


        return _bilinearform.BilinearForm_AddBdrFaceIntegrator(self, *args)


    def Assemble(self, skip_zeros=1):
        return _bilinearform.BilinearForm_Assemble(self, skip_zeros)

    def GetProlongation(self):
        return _bilinearform.BilinearForm_GetProlongation(self)

    def GetRestriction(self):
        return _bilinearform.BilinearForm_GetRestriction(self)

    def FormLinearSystem(self, ess_tdof_list, x, b, A, X, B, copy_interior=0):
        return _bilinearform.BilinearForm_FormLinearSystem(self, ess_tdof_list, x, b, A, X, B, copy_interior)

    def FormSystemMatrix(self, ess_tdof_list, A):
        return _bilinearform.BilinearForm_FormSystemMatrix(self, ess_tdof_list, A)

    def RecoverFEMSolution(self, X, b, x):
        return _bilinearform.BilinearForm_RecoverFEMSolution(self, X, b, x)

    def ComputeElementMatrices(self):
        return _bilinearform.BilinearForm_ComputeElementMatrices(self)

    def FreeElementMatrices(self):
        return _bilinearform.BilinearForm_FreeElementMatrices(self)

    def ComputeElementMatrix(self, i, elmat):
        return _bilinearform.BilinearForm_ComputeElementMatrix(self, i, elmat)

    def AssembleElementMatrix(self, i, elmat, vdofs, skip_zeros=1):
        return _bilinearform.BilinearForm_AssembleElementMatrix(self, i, elmat, vdofs, skip_zeros)

    def AssembleBdrElementMatrix(self, i, elmat, vdofs, skip_zeros=1):
        return _bilinearform.BilinearForm_AssembleBdrElementMatrix(self, i, elmat, vdofs, skip_zeros)

    def EliminateEssentialBC(self, *args):
        return _bilinearform.BilinearForm_EliminateEssentialBC(self, *args)

    def EliminateEssentialBCDiag(self, bdr_attr_is_ess, value):
        return _bilinearform.BilinearForm_EliminateEssentialBCDiag(self, bdr_attr_is_ess, value)

    def EliminateVDofs(self, *args):
        return _bilinearform.BilinearForm_EliminateVDofs(self, *args)

    def EliminateEssentialBCFromDofs(self, *args):
        return _bilinearform.BilinearForm_EliminateEssentialBCFromDofs(self, *args)

    def EliminateEssentialBCFromDofsDiag(self, ess_dofs, value):
        return _bilinearform.BilinearForm_EliminateEssentialBCFromDofsDiag(self, ess_dofs, value)

    def EliminateVDofsInRHS(self, vdofs, x, b):
        return _bilinearform.BilinearForm_EliminateVDofsInRHS(self, vdofs, x, b)

    def FullInnerProduct(self, x, y):
        return _bilinearform.BilinearForm_FullInnerProduct(self, x, y)

    def Update(self, nfes=None):
        return _bilinearform.BilinearForm_Update(self, nfes)

    def GetFES(self):
        return _bilinearform.BilinearForm_GetFES(self)

    def FESpace(self, *args):
        return _bilinearform.BilinearForm_FESpace(self, *args)
    __swig_destroy__ = _bilinearform.delete_BilinearForm
    __del__ = lambda self: None
BilinearForm_swigregister = _bilinearform.BilinearForm_swigregister
BilinearForm_swigregister(BilinearForm)

class MixedBilinearForm(matrix.Matrix):
    __swig_setmethods__ = {}
    for _s in [matrix.Matrix]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, MixedBilinearForm, name, value)
    __swig_getmethods__ = {}
    for _s in [matrix.Matrix]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, MixedBilinearForm, name)
    __repr__ = _swig_repr

    def __init__(self, tr_fes, te_fes):
        this = _bilinearform.new_MixedBilinearForm(tr_fes, te_fes)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def Elem(self, *args):
        return _bilinearform.MixedBilinearForm_Elem(self, *args)

    def Mult(self, x, y):
        return _bilinearform.MixedBilinearForm_Mult(self, x, y)

    def AddMult(self, x, y, a=1.0):
        return _bilinearform.MixedBilinearForm_AddMult(self, x, y, a)

    def AddMultTranspose(self, x, y, a=1.0):
        return _bilinearform.MixedBilinearForm_AddMultTranspose(self, x, y, a)

    def MultTranspose(self, x, y):
        return _bilinearform.MixedBilinearForm_MultTranspose(self, x, y)

    def Inverse(self):
        return _bilinearform.MixedBilinearForm_Inverse(self)

    def Finalize(self, skip_zeros=1):
        return _bilinearform.MixedBilinearForm_Finalize(self, skip_zeros)

    def GetBlocks(self, blocks):
        return _bilinearform.MixedBilinearForm_GetBlocks(self, blocks)

    def SpMat(self, *args):
        val = _bilinearform.MixedBilinearForm_SpMat(self, *args)

        if not hasattr(self, "_spmat"): self._spmat = []
        self._spmat.append(val)
        val.thisown=0 


        return val


    def LoseMat(self):
        return _bilinearform.MixedBilinearForm_LoseMat(self)

    def AddDomainIntegrator(self, bfi):

        if not hasattr(self, "_integrators"): self._integrators = []
        self._integrators.append(bfi)
        bfi.thisown=0 


        return _bilinearform.MixedBilinearForm_AddDomainIntegrator(self, bfi)


    def AddBoundaryIntegrator(self, bfi):

        if not hasattr(self, "_integrators"): self._integrators = []
        self._integrators.append(bfi)
        bfi.thisown=0 


        return _bilinearform.MixedBilinearForm_AddBoundaryIntegrator(self, bfi)


    def AddTraceFaceIntegrator(self, bfi):

        if not hasattr(self, "_integrators"): self._integrators = []
        self._integrators.append(bfi)
        bfi.thisown=0 


        return _bilinearform.MixedBilinearForm_AddTraceFaceIntegrator(self, bfi)


    def GetDBFI(self):
        return _bilinearform.MixedBilinearForm_GetDBFI(self)

    def GetBBFI(self):
        return _bilinearform.MixedBilinearForm_GetBBFI(self)

    def GetTFBFI(self):
        return _bilinearform.MixedBilinearForm_GetTFBFI(self)

    def Assemble(self, skip_zeros=1):
        return _bilinearform.MixedBilinearForm_Assemble(self, skip_zeros)

    def ConformingAssemble(self):
        return _bilinearform.MixedBilinearForm_ConformingAssemble(self)

    def EliminateTrialDofs(self, bdr_attr_is_ess, sol, rhs):
        return _bilinearform.MixedBilinearForm_EliminateTrialDofs(self, bdr_attr_is_ess, sol, rhs)

    def EliminateEssentialBCFromTrialDofs(self, marked_vdofs, sol, rhs):
        return _bilinearform.MixedBilinearForm_EliminateEssentialBCFromTrialDofs(self, marked_vdofs, sol, rhs)

    def EliminateTestDofs(self, bdr_attr_is_ess):
        return _bilinearform.MixedBilinearForm_EliminateTestDofs(self, bdr_attr_is_ess)

    def Update(self):
        return _bilinearform.MixedBilinearForm_Update(self)
    __swig_destroy__ = _bilinearform.delete_MixedBilinearForm
    __del__ = lambda self: None
MixedBilinearForm_swigregister = _bilinearform.MixedBilinearForm_swigregister
MixedBilinearForm_swigregister(MixedBilinearForm)

class DiscreteLinearOperator(MixedBilinearForm):
    __swig_setmethods__ = {}
    for _s in [MixedBilinearForm]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, DiscreteLinearOperator, name, value)
    __swig_getmethods__ = {}
    for _s in [MixedBilinearForm]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, DiscreteLinearOperator, name)
    __repr__ = _swig_repr

    def __init__(self, domain_fes, range_fes):
        this = _bilinearform.new_DiscreteLinearOperator(domain_fes, range_fes)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def AddDomainInterpolator(self, di):

        if not hasattr(self, "_integrators"): self._integrators = []
        self._integrators.append(di)
        di.thisown=0 


        return _bilinearform.DiscreteLinearOperator_AddDomainInterpolator(self, di)


    def AddTraceFaceInterpolator(self, di):

        if not hasattr(self, "_integrators"): self._integrators = []
        self._integrators.append(di)
        di.thisown=0 


        return _bilinearform.DiscreteLinearOperator_AddTraceFaceInterpolator(self, di)


    def GetDI(self):
        return _bilinearform.DiscreteLinearOperator_GetDI(self)

    def Assemble(self, skip_zeros=1):
        return _bilinearform.DiscreteLinearOperator_Assemble(self, skip_zeros)
    __swig_destroy__ = _bilinearform.delete_DiscreteLinearOperator
    __del__ = lambda self: None
DiscreteLinearOperator_swigregister = _bilinearform.DiscreteLinearOperator_swigregister
DiscreteLinearOperator_swigregister(DiscreteLinearOperator)

# This file is compatible with both classic and new-style classes.


