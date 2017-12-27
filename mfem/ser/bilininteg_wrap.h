/* ----------------------------------------------------------------------------
 * This file was automatically generated by SWIG (http://www.swig.org).
 * Version 3.0.12
 *
 * This file is not intended to be easily readable and contains a number of
 * coding conventions designed to improve portability and efficiency. Do not make
 * changes to this file unless you know what you are doing--modify the SWIG
 * interface file instead.
 * ----------------------------------------------------------------------------- */

#ifndef SWIG_bilininteg_WRAP_H_
#define SWIG_bilininteg_WRAP_H_

#include <map>
#include <string>


class SwigDirector_BilinearFormIntegrator : public mfem::BilinearFormIntegrator, public Swig::Director {

public:
    SwigDirector_BilinearFormIntegrator(PyObject *self, mfem::IntegrationRule const *ir = NULL);
    virtual void AssembleElementMatrix(mfem::FiniteElement const &el, mfem::ElementTransformation &Trans, mfem::DenseMatrix &elmat);
    virtual void AssembleElementMatrix2(mfem::FiniteElement const &trial_fe, mfem::FiniteElement const &test_fe, mfem::ElementTransformation &Trans, mfem::DenseMatrix &elmat);
    virtual void AssembleFaceMatrix(mfem::FiniteElement const &el1, mfem::FiniteElement const &el2, mfem::FaceElementTransformations &Trans, mfem::DenseMatrix &elmat);
    virtual void AssembleFaceMatrix(mfem::FiniteElement const &trial_face_fe, mfem::FiniteElement const &test_fe1, mfem::FiniteElement const &test_fe2, mfem::FaceElementTransformations &Trans, mfem::DenseMatrix &elmat);
    virtual void AssembleElementVector(mfem::FiniteElement const &el, mfem::ElementTransformation &Tr, mfem::Vector const &elfun, mfem::Vector &elvect);
    virtual void AssembleElementGrad(mfem::FiniteElement const &el, mfem::ElementTransformation &Tr, mfem::Vector const &elfun, mfem::DenseMatrix &elmat);
    virtual void AssembleFaceGrad(mfem::FiniteElement const &el1, mfem::FiniteElement const &el2, mfem::FaceElementTransformations &Tr, mfem::Vector const &elfun, mfem::DenseMatrix &elmat);
    virtual void ComputeElementFlux(mfem::FiniteElement const &el, mfem::ElementTransformation &Trans, mfem::Vector &u, mfem::FiniteElement const &fluxelem, mfem::Vector &flux, int with_coef = 1);
    virtual double ComputeFluxEnergy(mfem::FiniteElement const &fluxelem, mfem::ElementTransformation &Trans, mfem::Vector &flux, mfem::Vector *d_energy = NULL);
    virtual ~SwigDirector_BilinearFormIntegrator();

/* Internal director utilities */
public:
    bool swig_get_inner(const char *swig_protected_method_name) const {
      std::map<std::string, bool>::const_iterator iv = swig_inner.find(swig_protected_method_name);
      return (iv != swig_inner.end() ? iv->second : false);
    }
    void swig_set_inner(const char *swig_protected_method_name, bool swig_val) const {
      swig_inner[swig_protected_method_name] = swig_val;
    }
private:
    mutable std::map<std::string, bool> swig_inner;

#if defined(SWIG_PYTHON_DIRECTOR_VTABLE)
/* VTable implementation */
    PyObject *swig_get_method(size_t method_index, const char *method_name) const {
      PyObject *method = vtable[method_index];
      if (!method) {
        swig::SwigVar_PyObject name = SWIG_Python_str_FromChar(method_name);
        method = PyObject_GetAttr(swig_get_self(), name);
        if (!method) {
          std::string msg = "Method in class BilinearFormIntegrator doesn't exist, undefined ";
          msg += method_name;
          Swig::DirectorMethodException::raise(msg.c_str());
        }
        vtable[method_index] = method;
      }
      return method;
    }
private:
    mutable swig::SwigVar_PyObject vtable[11];
#endif

};


#endif
