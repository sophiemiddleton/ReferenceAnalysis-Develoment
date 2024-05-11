CC=`root-config --cxx`
CFLAGS=`root-config --cflags` -g -Wall
LDFLAGS=`root-config --glibs` -lMinuit2 -lRooStats -lRooFit  -lRooFitCore
SOURCES=Mu2eAna.cc  Likelihood.cc MyDict.cc
OBJECTS=$(SOURCES:.cc=.o)
HEADERS=Mu2eAna.hh  Likelihood.hh RooPol58.hh
EXECUTABLE=Mu2eAna

all: $(EXECUTABLE)

$(EXECUTABLE): $(OBJECTS)
	$(CC) $(CFLAGS) -o $@ $(OBJECTS) $(LDFLAGS)

MyDict.cc: $(HEADERS) LinkDef.h
	rootcling -f $@ -c $(CXXFLAGS) -p $^

.cc.o:
	$(CC) $(CFLAGS) -c $< -o $@

clean:
	rm -f ./*~ ./*.o ./MyDict.* ./$(EXECUTABLE)
