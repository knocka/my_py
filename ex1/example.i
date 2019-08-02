/* example.i */
#ifdef SWIG
%module example
%{
 /* Put header files here or function declarations like below */
#include "example.h"
#include "word.h"
%}
#endif
 
/*extern double My_variable;*/
%include "std_string.i"
%include "example.h"
%include "word.h"
