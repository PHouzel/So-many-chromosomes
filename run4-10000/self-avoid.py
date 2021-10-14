# Initializate the simulation initial state and parameters

import random
import math
import numpy as np

global tmax
length = 25
dims = 3
tmax = 9999
t = 0

x = [0]
y = [0]
z = [0]


t=0
t_total = 0
coodr = [[x[t],y[t],z[t]]]
xcord = [0]
ycord = [0]
zcord= [0]
dist = 0
left = True
up  = True
right = True
down = True
front = True
behind = True
while t < tmax:# and t_total < tmax:
    #    print(len(x) ,  len(y) , len(coodr))
    if [(x[t]-1),y[t],z[t]] in coodr:
        left = False
    else:
        left = True
    if [(x[t]+1),y[t],z[t]] in coodr:
        right = False
    else:
        right = True
    if [(x[t]),(y[t]+1),z[t]] in coodr:
        front = False
    else:
        front = True
    if [(x[t]),(y[t]-1),z[t]] in coodr:
        behind = False
    else:
        behind = True
    if [(x[t]),(y[t]),(z[t]+1)] in coodr:
        up = False
    else:
        up = True
    if [(x[t]),(y[t]),(z[t]-1)] in coodr:
        down = False
    else:
        down = True

    all_dir = [left, front,right, behind, up,  down]
    #    print(all_dir)
    available_dir = []
    i=0
    for dir in all_dir:
        if dir == True:
            available_dir.append(i)
        i=i+1
    #    print(available_dir)
    if t % 10 == 0:
        if len(available_dir) == 5:
            left_inf = []
            up_inf = []
            right_inf = []
            down_inf = []
            front_inf = []
            behind_inf = []
            for j in range(0,100):
                #for j in range(0, tmax):
                left_inf.append([x[t]-j,y[t],z[t]] )
                front_inf.append([x[t],y[t]+j,z[t]] )
                right_inf.append([x[t]+j,y[t],z[t]] )
                behind_inf.append([x[t],y[t]-j,z[t]] )
                up_inf.append([x[t],y[t],z[t]+j] )
                down_inf.append([x[t],y[t],z[t]-j] )
            #    left_inf_tuple = [tuple(lst) for lst in left_inf]
            left_inf_tuple = set(map(tuple, left_inf))
            up_inf_tuple = set(map(tuple, up_inf))
            right_inf_tuple = set(map(tuple, right_inf))
            down_inf_tuple = set(map(tuple, down_inf))
            front_inf_tuple = set(map(tuple, front_inf))
            behind_inf_tuple = set(map(tuple, behind_inf))
            coord_tuple = set(map(tuple, coodr))
            #    print("types")
            #    print(type(left_inf_tuple))
            #    print(type((coord_tuple)) )
            #    print((left_inf_tuple).intersection(coord_tuple))
            if  (left_inf_tuple).intersection(coord_tuple) == set():
                #if (any(i in left_inf_tuple for j in coord_tuple)):
                #    print(left_inf_tuple)
                #    print([x[t] , y[t]])
                #    print(coord_tuple)
                    #print(left_inf)
                #    print("left is safe")
                safe_t = t
            elif  (up_inf_tuple).intersection(coord_tuple) == set():
                #    print("up is safe")
                safe_t = t
            elif  (right_inf_tuple).intersection(coord_tuple) == set():
                #    print("right is safe")
                safe_t = t
            elif  (down_inf_tuple).intersection(coord_tuple) == set():
                #    print("down is safe")
                safe_t = t
            elif  (front_inf_tuple).intersection(coord_tuple) == set():
                #    print("front is safe")
                safe_t = t
            elif (behind_inf_tuple).intersection(coord_tuple) == set():
                #    print("behind is safe")
                safe_t = t
                    
        #    safe_t = t
        #    print(t)
        #    print("tsafe = " + str(safe_t))
    if not available_dir:
            #print("backtracking...")
        t_diff = t - safe_t
        t = safe_t
            #print("went back " + str(t_diff) + " steps")
        coodr=coodr[:-(t_diff)]
        x = x[:-(t_diff)]
        y = y[:(-(t_diff))]
        z = z[:-(t_diff)]

            #print("current length " + str(len(x)))
    else:
        chosen_dir = random.choice(available_dir)
        if chosen_dir == 0:
            x.append(x[t]-1)
            y.append(y[t])
            z.append(z[t])
        elif chosen_dir == 1:
            x.append(x[t])
            y.append(y[t]+1)
            z.append(z[t])
        elif chosen_dir == 2:
            x.append(x[t]+1)
            y.append(y[t])
            z.append(z[t])
        elif chosen_dir == 3:
            x.append(x[t])
            y.append(y[t]-1)
            z.append(z[t])
        elif chosen_dir == 4:
            x.append(x[t])
            y.append(y[t])
            z.append(z[t]+1)
        elif chosen_dir == 5:
            x.append(x[t])
            y.append(y[t])
            z.append(z[t]-1)


        cur_dist = x[t]*x[t]+y[t]*y[t]+z[t]*z[t]
        if cur_dist > dist:
            dist = cur_dist
        coodr.append([x[t],y[t],z[t]])
        t=t+1
    t_total = t_total + 1     
        
        
atom_id = 0
mol_id = 0

natoms= len(x)
box_x = np.max(np.absolute([x,y,z]))*5
mass_atom = 14
nparts = 1

with open('data5','w') as fout:
    fout.write("LAMMPS data file\n\n%d atoms\n%d bonds\n%d angles\n\n1 atom types\n1 bond types\n1 angle types\n\n0.0 %f xlo xhi\n0.0 %f ylo yhi\n0.0 %f zlo zhi\n\nMasses\n\n1 %f\n\nAtoms\n\n"%(natoms,natoms-1, natoms-2,box_x,box_x,box_x,mass_atom))
    
    for j in range(0,nparts):
        mol_id+=1
        
        for i in range(0,len(x)):
            atom_id+=1
            fout.write("%d %d 1 %.15f %.15f %.15f\n"%(atom_id,mol_id,x[i],y[i],z[i]))
            
    fout.write("\nBonds\n\n")
    atom_id = 0
    mol_id = 0
    
    for j in range(0,nparts):
        mol_id+=1
        
        for i in range(1,len(x)):
            atom_id+=1
            bond1 = i
            bond2 = i+1
            fout.write("%d 1 %d %d\n"%(atom_id,bond1,bond2))
            
                
    fout.write("\nAngles\n\n")
    atom_id = 0
    mol_id = 0
    
    for j in range(0,nparts):
        mol_id+=1
        
        for i in range(1,len(x)-1):
            atom_id+=1
            angle1 = i
            angle2 = i+1
            angle3 = i+2
            fout.write("%d 1 %d %d %d\n"%(atom_id,angle1,angle2, angle3))