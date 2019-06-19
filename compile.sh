#!/bin/bash

rm -rf CMakeFiles/ CMakeCache.txt 
cmake -DCMAKE_BUILD_TYPE=Release
make -j 2
