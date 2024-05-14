# ReferenceAnalysis-Develoment

## Purpose 

The purpose of the Referene Analysis is to quantify changes in our assumed physics reach as we update our reconstruction and/or simulation code.

It provides a simple cross-check, and also a place to exercise our analysis toolkit.

## Analysis Strategy

Scripts associated with development of the Mu2e Reference Analysis

* ReferenceAna - this runs roofit on standard ntuple (currently TrkAna) output on Mu2e machines;
* StatsTool-CutNCount - this will priovide a simplistic cut-and-count analysis - currently a set of python scripts interfaced to pyROOT.

## Development Status

Both these tools are under-development. Here is the current status:

### ReferenceAna

currently operatonal: it compiles and provides meaningful results (see README in that repo). It currently runs a ML fit with an extended, binned likelihood. The Likelihood is a sum of PDF contributions from CE, DIO and cosmics in momentum space only. 

There is also the functionality to create the -logL and a profile -logL, this will be more useful when we begin to introduce nuisance parameters.

There is room to contribute here: reach out to volunteer (smidd@caltech.edu)

### StatsTool-CutNCount

this is currently under-development. These scripts are from the StatsTool 2021 package made for the Mu2e-II study. They need heavily updating.

There is room to contribute here: reach out to volunteer (smidd@caltech.edu)
