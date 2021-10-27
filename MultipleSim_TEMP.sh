#!/bin/bash

N_ITER=5
SIM_NAME=run2-1000
DIR_NAME=dumplin1000_A100_cluster
DUMPLIN_NAME=dumplin1000_K100

echo "Arguments: "
echo $SIM_NAME
echo $DIR_NAME
echo $DUMPLIN_NAME

cd $SIM_NAME
mkdir $DIR_NAME

for iter in {1..$N_ITER}
do
	python3 self-avoid.py
   mpirun -n 6 lmp -in polymer-descript.in 
   cp -R dumplin $DIR_NAME
   cd $DIR_NAME
   mv dumplin $DUMPLIN_NAME_$iter
   cd ..
done

echo "Everything went fine, I take a nap now."