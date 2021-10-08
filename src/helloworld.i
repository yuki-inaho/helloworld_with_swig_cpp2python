%module hello_world
%{
#define SWIG_FILE_WITH_INIT
#include "helloworld.h"
%}

extern void HelloWorld ();