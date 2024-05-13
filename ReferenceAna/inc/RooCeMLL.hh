#ifndef RooCeMLL_h_
#define RooCeMLL_h_

/*
Functional form of the Szafaron parameterization of the conversion signal with leading log corrections
*/
#include "RooAbsPdf.h"
#include "RooRealProxy.h"
#include "RooCategoryProxy.h"
#include "RooAbsReal.h"
#include "RooAbsCategory.h"

class RooCeMLL : public RooAbsPdf {
public:
  RooCeMLL() {} ; 
  RooCeMLL(const char *name, const char *title, RooAbsReal& _x, RooAbsReal& _eMax, RooAbsReal& _me, RooAbsReal& _alpha) :
    RooAbsPdf(name,title), 
    x("x","x",this,_x),
    eMax("eMax","eMax",this,_eMax),
    me("me","me",this,_me),
    alpha("alpha","alpha",this,_alpha)
  {}

  RooCeMLL(const RooCeMLL& other, const char* name=0) :
    RooAbsPdf(other,name), 
    x("x",this,other.x),
    eMax("eMax",this,other.eMax),
    me("me",this,other.me),
    alpha("alpha",this,other.alpha)
  {}

  virtual TObject* clone(const char* newname) const { return new RooCeMLL(*this,newname); }
  inline virtual ~RooCeMLL() { }
  
protected:
  
  RooRealProxy x ;
  RooRealProxy eMax ;
  RooRealProxy me ;
  RooRealProxy alpha ;

  Double_t evaluate() const {
    double E = std::sqrt(x*x + me*me);
    double result = (1./eMax)*(alpha/(2*M_PI))*(log(4*E*E/me/me)-2.)*((E*E+eMax*eMax)/eMax/(eMax-E));
    if (result < 0) {
      result = 0;
    }
    return result;
  }
  
  
  ClassDef(RooCeMLL,1) // Your description goes here...
};
 
#endif
