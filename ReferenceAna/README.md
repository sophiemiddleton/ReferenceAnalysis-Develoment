# ReferenceAna Framework
 This code is meant for the analysis of reconstructed Mu2e data or MC.


To build:

```
muse build
```

Then:

```
./build/sl7-prof-e28-p056/ReferenceAna/bin/ReferenceAna nts.mu2e.ensemble-1BB-CEDIOCRYCosmic-600000s-p95MeVc-Triggered.MDC2024.0.tka "pass0b" true "unbinned"


```

## Input parameters

in the above command:

* /build/sl7-prof-e28-p056/ReferenceAna/bin/ReferenceAna is the built executable
* nts.mu2e.ensemble-1BB-CEDIOCRYCosmic-600000s-p95MeVc-Triggered.MDC2024.0.tka is the filename
* pass0b is the run name
* true says to "usecuts"
* unbinned describes the fit type



# Classes:

* Likelihood - will build up the likelihood
* RooPol58 - DIO momentum custom PDF
