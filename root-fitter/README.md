# Mu2eAna Framework
Code written by Sophie Middleton (Caltech). This code is meant for the analysis of reconstructed Mu2e data or MC.


To build:

```
make clean
make all
```

Then:

```
./Mu2eAna "filename" "pass0a" true

```


To clean:

```
make clean
```

# Classes:

* Likelihood - will build up the likelihood
* Nusiance - will build up nusiance parameters and pass to Likelihood
* RooPol58 - DIO momentum custom PDF
