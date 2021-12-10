#!/bin/bash

# Run multiple simulations with these parameters
# Care: dumplin and dumplin_image must be present and empty.
# No dumplin_cluster and dumplin_cluster_image can appear.

N_ITER=10
SIM_NAME=run2-1000
DIR_NAME=dumplin_cluster
DIR_NAME_IMAGE=dumplin_cluster_image
DIR_NAME_RG_CLUSTER=rad_gyr_cluster
DIR_NAME_RG=rad_gyr
DUMPLIN_NAME=dumplin
DUMPLIN_NAME_IMAGE=dumplin_image
py_NAME=wall-avoid.py
in_NAME=polymer-wall.in

bar=_
echo "Arguments: "
echo $SIM_NAME
echo $DIR_NAME
echo $py_NAME
echo $in_NAME


cd $SIM_NAME
mkdir $DIR_NAME
mkdir $DIR_NAME_IMAGE
mkdir $DIR_NAME_RG_CLUSTER

for (( iter=1; iter<=N_ITER; iter++ ))
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
   cd $DIR_NAME_RG_CLUSTER
   mkdir $DIR_NAME_RG$bar$iter
   cd ..

   cp -R dumplin $DIR_NAME/$DUMPLIN_NAME$bar$iter
   cp -R dumplin_image $DIR_NAME_IMAGE/$DUMPLIN_NAME_IMAGE$bar$iter
   
   cp radius_of_gyration_squared.dat $DIR_NAME_RG_CLUSTER/$DIR_NAME_RG$bar$iter

   # Delete old run files
   rm dumplin/*
   rm dumplin_image/*
done

echo "Everything went fine, I take a nap now."