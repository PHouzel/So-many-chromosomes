#!/bin/bash

# run multiple simulation with these parameters
N_ITER=2
SIM_NAME=run2-1000
DIR_NAME=dumplin_cluster
DIR_NAME_IMAGE=dumplin_cluster_image
DUMPLIN_NAME=dumplin
DUMPLIN_NAME_IMAGE=dumplin_image
py_NAME=self-avoid.py
in_NAME=polymer-descript.in

bar=_
echo "Arguments: "
echo $SIM_NAME
echo $DIR_NAME
echo $py_NAME
echo $in_NAME


cd $SIM_NAME
mkdir $DIR_NAME
mkdir $DIR_NAME_IMAGE

for (( iter=1; iter<=2; iter++ ))
do
   # Execute
	python3 $py_NAME
   mpirun -n 6 lmp -in $in_NAME
   # Move output files
   cd $DIR_NAME
   mkdir $DUMPLIN_NAME$bar$iter
   cd ..
   cd $DIR_NAME_IMAGE
   mkdir $DUMPLIN_NAME_IMAGE$bar$iter
   cd ..

   cp -R dumplin $DIR_NAME/$DUMPLIN_NAME$bar$iter
   cp -R dumplin_image $DIR_NAME_IMAGE/$DUMPLIN_NAME_IMAGE$bar$iter

   # Delete old run files
   rm dumplin/*
   rm dumplin_image/*
done

echo "Everything went fine, I take a nap now."