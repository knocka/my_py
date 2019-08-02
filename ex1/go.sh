#!/bin/bash
swig -Wall -c++ -python example.i
#gcc -c example.c example_wrap.c -I /usr/include/python2.7
g++ -fpic -c example.h example_wrap.cxx word.cpp -I/usr/include/python2.7
#ld -shared example.o example_wrap.o -o _example.so
g++ -shared example.o example_wrap.o word.o -o _example.so -lstdc++
python run.py
