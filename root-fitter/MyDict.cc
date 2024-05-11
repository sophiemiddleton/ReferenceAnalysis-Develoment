// Do NOT change. Changes will be lost next time file is generated

#define R__DICTIONARY_FILENAME MyDict
#define R__NO_DEPRECATION

/*******************************************************************/
#include <stddef.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <assert.h>
#define G__DICTIONARY
#include "ROOT/RConfig.hxx"
#include "TClass.h"
#include "TDictAttributeMap.h"
#include "TInterpreter.h"
#include "TROOT.h"
#include "TBuffer.h"
#include "TMemberInspector.h"
#include "TInterpreter.h"
#include "TVirtualMutex.h"
#include "TError.h"

#ifndef G__ROOT
#define G__ROOT
#endif

#include "RtypesImp.h"
#include "TIsAProxy.h"
#include "TFileMergeInfo.h"
#include <algorithm>
#include "TCollectionProxyInfo.h"
/*******************************************************************/

#include "TDataMember.h"

// Header files passed as explicit arguments
#include "Mu2eAna.hh"
#include "Likelihood.hh"
#include "RooPol58.hh"

// Header files passed via #pragma extra_include

// The generated code does not explicitly qualify STL entities
namespace std {} using namespace std;

namespace ROOT {
   static void *new_RooPol58(void *p = nullptr);
   static void *newArray_RooPol58(Long_t size, void *p);
   static void delete_RooPol58(void *p);
   static void deleteArray_RooPol58(void *p);
   static void destruct_RooPol58(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::RooPol58*)
   {
      ::RooPol58 *ptr = nullptr;
      static ::TVirtualIsAProxy* isa_proxy = new ::TInstrumentedIsAProxy< ::RooPol58 >(nullptr);
      static ::ROOT::TGenericClassInfo 
         instance("RooPol58", ::RooPol58::Class_Version(), "RooPol58.hh", 13,
                  typeid(::RooPol58), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &::RooPol58::Dictionary, isa_proxy, 4,
                  sizeof(::RooPol58) );
      instance.SetNew(&new_RooPol58);
      instance.SetNewArray(&newArray_RooPol58);
      instance.SetDelete(&delete_RooPol58);
      instance.SetDeleteArray(&deleteArray_RooPol58);
      instance.SetDestructor(&destruct_RooPol58);
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::RooPol58*)
   {
      return GenerateInitInstanceLocal(static_cast<::RooPol58*>(nullptr));
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_DICT_(Init) = GenerateInitInstanceLocal(static_cast<const ::RooPol58*>(nullptr)); R__UseDummy(_R__UNIQUE_DICT_(Init));
} // end of namespace ROOT

namespace ROOT {
   static void *new_Likelihood(void *p = nullptr);
   static void *newArray_Likelihood(Long_t size, void *p);
   static void delete_Likelihood(void *p);
   static void deleteArray_Likelihood(void *p);
   static void destruct_Likelihood(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::Likelihood*)
   {
      ::Likelihood *ptr = nullptr;
      static ::TVirtualIsAProxy* isa_proxy = new ::TInstrumentedIsAProxy< ::Likelihood >(nullptr);
      static ::ROOT::TGenericClassInfo 
         instance("Likelihood", ::Likelihood::Class_Version(), "Likelihood.hh", 53,
                  typeid(::Likelihood), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &::Likelihood::Dictionary, isa_proxy, 4,
                  sizeof(::Likelihood) );
      instance.SetNew(&new_Likelihood);
      instance.SetNewArray(&newArray_Likelihood);
      instance.SetDelete(&delete_Likelihood);
      instance.SetDeleteArray(&deleteArray_Likelihood);
      instance.SetDestructor(&destruct_Likelihood);
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::Likelihood*)
   {
      return GenerateInitInstanceLocal(static_cast<::Likelihood*>(nullptr));
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_DICT_(Init) = GenerateInitInstanceLocal(static_cast<const ::Likelihood*>(nullptr)); R__UseDummy(_R__UNIQUE_DICT_(Init));
} // end of namespace ROOT

//______________________________________________________________________________
atomic_TClass_ptr RooPol58::fgIsA(nullptr);  // static to hold class pointer

//______________________________________________________________________________
const char *RooPol58::Class_Name()
{
   return "RooPol58";
}

//______________________________________________________________________________
const char *RooPol58::ImplFileName()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::RooPol58*)nullptr)->GetImplFileName();
}

//______________________________________________________________________________
int RooPol58::ImplFileLine()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::RooPol58*)nullptr)->GetImplFileLine();
}

//______________________________________________________________________________
TClass *RooPol58::Dictionary()
{
   fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::RooPol58*)nullptr)->GetClass();
   return fgIsA;
}

//______________________________________________________________________________
TClass *RooPol58::Class()
{
   if (!fgIsA.load()) { R__LOCKGUARD(gInterpreterMutex); fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::RooPol58*)nullptr)->GetClass(); }
   return fgIsA;
}

//______________________________________________________________________________
atomic_TClass_ptr Likelihood::fgIsA(nullptr);  // static to hold class pointer

//______________________________________________________________________________
const char *Likelihood::Class_Name()
{
   return "Likelihood";
}

//______________________________________________________________________________
const char *Likelihood::ImplFileName()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::Likelihood*)nullptr)->GetImplFileName();
}

//______________________________________________________________________________
int Likelihood::ImplFileLine()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::Likelihood*)nullptr)->GetImplFileLine();
}

//______________________________________________________________________________
TClass *Likelihood::Dictionary()
{
   fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::Likelihood*)nullptr)->GetClass();
   return fgIsA;
}

//______________________________________________________________________________
TClass *Likelihood::Class()
{
   if (!fgIsA.load()) { R__LOCKGUARD(gInterpreterMutex); fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::Likelihood*)nullptr)->GetClass(); }
   return fgIsA;
}

//______________________________________________________________________________
void RooPol58::Streamer(TBuffer &R__b)
{
   // Stream an object of class RooPol58.

   if (R__b.IsReading()) {
      R__b.ReadClassBuffer(RooPol58::Class(),this);
   } else {
      R__b.WriteClassBuffer(RooPol58::Class(),this);
   }
}

namespace ROOT {
   // Wrappers around operator new
   static void *new_RooPol58(void *p) {
      return  p ? new(p) ::RooPol58 : new ::RooPol58;
   }
   static void *newArray_RooPol58(Long_t nElements, void *p) {
      return p ? new(p) ::RooPol58[nElements] : new ::RooPol58[nElements];
   }
   // Wrapper around operator delete
   static void delete_RooPol58(void *p) {
      delete (static_cast<::RooPol58*>(p));
   }
   static void deleteArray_RooPol58(void *p) {
      delete [] (static_cast<::RooPol58*>(p));
   }
   static void destruct_RooPol58(void *p) {
      typedef ::RooPol58 current_t;
      (static_cast<current_t*>(p))->~current_t();
   }
} // end of namespace ROOT for class ::RooPol58

//______________________________________________________________________________
void Likelihood::Streamer(TBuffer &R__b)
{
   // Stream an object of class Likelihood.

   if (R__b.IsReading()) {
      R__b.ReadClassBuffer(Likelihood::Class(),this);
   } else {
      R__b.WriteClassBuffer(Likelihood::Class(),this);
   }
}

namespace ROOT {
   // Wrappers around operator new
   static void *new_Likelihood(void *p) {
      return  p ? new(p) ::Likelihood : new ::Likelihood;
   }
   static void *newArray_Likelihood(Long_t nElements, void *p) {
      return p ? new(p) ::Likelihood[nElements] : new ::Likelihood[nElements];
   }
   // Wrapper around operator delete
   static void delete_Likelihood(void *p) {
      delete (static_cast<::Likelihood*>(p));
   }
   static void deleteArray_Likelihood(void *p) {
      delete [] (static_cast<::Likelihood*>(p));
   }
   static void destruct_Likelihood(void *p) {
      typedef ::Likelihood current_t;
      (static_cast<current_t*>(p))->~current_t();
   }
} // end of namespace ROOT for class ::Likelihood

namespace {
  void TriggerDictionaryInitialization_MyDict_Impl() {
    static const char* headers[] = {
"Mu2eAna.hh",
"Likelihood.hh",
"RooPol58.hh",
nullptr
    };
    static const char* includePaths[] = {
"/cvmfs/mu2e.opensciencegrid.org/artexternals/root/v6_28_10a/Linux64bit+3.10-2.17-e28-p3915-prof/include/",
"/exp/mu2e/app/users/sophie/ProductionEnsembles_v2/ReferenceAnalysis-Develoment/root-fitter/",
nullptr
    };
    static const char* fwdDeclCode = R"DICTFWDDCLS(
#line 1 "MyDict dictionary forward declarations' payload"
#pragma clang diagnostic ignored "-Wkeyword-compat"
#pragma clang diagnostic ignored "-Wignored-attributes"
#pragma clang diagnostic ignored "-Wreturn-type-c-linkage"
extern int __Cling_AutoLoading_Map;
class __attribute__((annotate("$clingAutoload$RooPol58.hh")))  __attribute__((annotate("$clingAutoload$Mu2eAna.hh")))  RooPol58;
class __attribute__((annotate("$clingAutoload$Likelihood.hh")))  __attribute__((annotate("$clingAutoload$Mu2eAna.hh")))  Likelihood;
)DICTFWDDCLS";
    static const char* payloadCode = R"DICTPAYLOAD(
#line 1 "MyDict dictionary payload"


#define _BACKWARD_BACKWARD_WARNING_H
// Inline headers
#include "Mu2eAna.hh"
#include "Likelihood.hh"
#include "RooPol58.hh"

#undef  _BACKWARD_BACKWARD_WARNING_H
)DICTPAYLOAD";
    static const char* classesHeaders[] = {
"Likelihood", payloadCode, "@",
"RooPol58", payloadCode, "@",
nullptr
};
    static bool isInitialized = false;
    if (!isInitialized) {
      TROOT::RegisterModule("MyDict",
        headers, includePaths, payloadCode, fwdDeclCode,
        TriggerDictionaryInitialization_MyDict_Impl, {}, classesHeaders, /*hasCxxModule*/false);
      isInitialized = true;
    }
  }
  static struct DictInit {
    DictInit() {
      TriggerDictionaryInitialization_MyDict_Impl();
    }
  } __TheDictionaryInitializer;
}
void TriggerDictionaryInitialization_MyDict() {
  TriggerDictionaryInitialization_MyDict_Impl();
}
