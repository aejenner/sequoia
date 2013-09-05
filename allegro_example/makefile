#This is a makefile that should build on OS X, assuming you have allegro

GCC=gcc
BASE=sq7
OPS=-Wall
INCDIR=-I/usr/include -Iinclude/
LIBDIR=-L/usr/lib
FRAMEWORKS=-framework AudioToolbox -framework IOKit -framework OpenAL -framework OpenGL -framework Cocoa
LINKS= -lallegro-static -lallegro_main-static -lallegro_image-static -lallegro_audio-static -lallegro_acodec-static
SRCDIR=src/
BINDIR=bin/
RSCDIR=Resources/

all:
	$(GCC) $(OPS) $(INCDIR) $(LIBDIR) $(SRCDIR)*.c $(FRAMEWORKS) $(LINKS) -o $(BINDIR)$(BASE)
	cp $(BINDIR)$(BASE) $(BASE).app/Contents/MacOS/$(BASE)
	cp $(RSCDIR)* $(BASE).app/Contents/Resources/
