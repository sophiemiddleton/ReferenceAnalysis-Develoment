#ifndef _RooPol58_HH
#define _RooPol58_HH

/*
Class to call the pol5-8 Czernecki et al parameterization for DIO tail (assumes Al)
*/
#include "RooAbsPdf.h"
#include "RooRealProxy.h"
#include "RooCategoryProxy.h"
#include "RooAbsReal.h"
#include "RooAbsCategory.h"
 
class RooPol58 : public RooAbsPdf {
  public:
    RooPol58() {} ; 
    RooPol58(const char *name, const char *title,RooAbsReal& _x, RooAbsReal& _c5, RooAbsReal& _c6, RooAbsReal& _c7, RooAbsReal& _c8) :
     RooAbsPdf(name,title), 
     x("x","x",this,_x),
     c5("c5","c5",this,_c5),
     c6("c6","c6",this,_c6),
     c7("c7","c7",this,_c7),
     c8("c8","c8",this,_c8){}

    RooPol58(const RooPol58& other, const char* name=0) :
     RooAbsPdf(other,name), 
     x("x",this,other.x),
     c5("c5",this,other.c5),
     c6("c6",this,other.c6),
     c7("c7",this,other.c7),
     c8("c8",this,other.c8){}

    virtual TObject* clone(const char* newname) const { return new RooPol58(*this,newname); }
    inline virtual ~RooPol58() { }

  protected:

    RooRealProxy x ;
    RooRealProxy c5 ;
    RooRealProxy c6 ;
    RooRealProxy c7 ;
    RooRealProxy c8 ;
    
    Double_t evaluate() const {
      double muon_energy = 105.194;
      double atomic_mass = 26.981539*931.494095;
      double end_point = muon_energy - (muon_energy*muon_energy)/(2*atomic_mass);
      
      if (x > end_point){
        return 0.0;
      }
      
      double delta = muon_energy - x - (x*x)/(2*atomic_mass);
      double result = (c5*std::pow(delta, 5) + c6*std::pow(delta, 6) + c7*std::pow(delta, 7) + c8*std::pow(delta, 8));
      return result; 
    }


  private:

    ClassDef(RooPol58,1) // Your description goes here...
};
 
#endif
