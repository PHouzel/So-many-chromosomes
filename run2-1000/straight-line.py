# Initializate the simulation initial state and parameters

import random
import math
import numpy as np

global tmax
length = 25
dims = 3
tmax = 1199
        
atom_id = 0
mol_id = 0

natoms= tmax+1
box_x = 2*natoms
mass_atom = 14
nparts = 1

with open('data5','w') as fout:
    fout.write("LAMMPS data file\n\n%d atoms\n%d bonds\n%d angles\n\n1 atom types\n1 bond types\n1 angle types\n\n0.0 %f xlo xhi\n0.0 %f ylo yhi\n0.0 %f zlo zhi\n\nMasses\n\n1 %f\n\nAtoms\n\n"%(natoms,natoms-1, natoms-2,box_x/4,box_x,box_x/4,mass_atom))
    
    for j in range(0,nparts):
        mol_id+=1
        
        for i in range(0,natoms):
            atom_id+=1
            fout.write("%d %d 1 %.15f %.15f %.15f\n"%(atom_id,mol_id,0,i,0))
            
    fout.write("\nBonds\n\n")
    atom_id = 0
    mol_id = 0
    
    for j in range(0,nparts):
        mol_id+=1
        
        for i in range(1,natoms):
            atom_id+=1
            bond1 = i
            bond2 = i+1
            fout.write("%d 1 %d %d\n"%(atom_id,bond1,bond2))
            
                
    fout.write("\nAngles\n\n")
    atom_id = 0
    mol_id = 0
    
    for j in range(0,nparts):
        mol_id+=1
        
        for i in range(1,natoms-1):
            atom_id+=1
            angle1 = i
            angle2 = i+1
            angle3 = i+2
            fout.write("%d 1 %d %d %d\n"%(atom_id,angle1,angle2, angle3))