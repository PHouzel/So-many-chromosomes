#!/bin/bash

SIM_NAME=run2-1000

cd $SIM_NAME
for iter in {1..20}
do
	python3 self-avoid.py
   mpirun -n 6 lmp -in polymer-descript.in 
   cp -R dumplin dumplin_cluster
   cd dumplin_cluster
   mv dumplin dumplin$iter
   cd ..
done