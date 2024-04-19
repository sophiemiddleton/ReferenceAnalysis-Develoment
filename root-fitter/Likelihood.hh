#ifndef _Likelihood_HH
#define _Likelihood_HH

// ROOT:
#include <TObjString.h>
#include <TROOT.h>
#include <TSystem.h>
#include <TMath.h>

using namespace std;

class Likelihood  {
  public:
    #ifndef __CINT__
    explicit Likelihood(){};
    Likelihood(const Likelihood &);
    Likelihood& operator=(const Likelihood &);
    virtual ~Likelihood() = default;
    double CalculateLikelihood(double u);
    #endif
    ClassDef (Likelihood,0);

};

#endif /* Likelihood.hh */
