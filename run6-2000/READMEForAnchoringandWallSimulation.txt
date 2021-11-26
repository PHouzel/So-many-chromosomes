2000 atoms, 1 wall (yz plane, reflecting in dir of positive x), anchoring of the point 1 in the center of the "box". 

anchoring-1wall-avoid.py 
Generate the 2000 atoms double branch structure in the positive x subspace. 
The whole polymer is shifted to the center of the region occupied (for visualisation reasons)

polymer-anchoring-1wall.in 
evolve the simulation in a box with walls in yz planes (on both sides of the box).
periodic BCs on the remaining sides, set far away from the polymer.
This script needs the presence of 2 directories: dumplin (for traj files) and dumplin_image (image output)

wall-avoid.py
conceptually is only the generation of the chain inside a box of fixed size

polymer-wall.in
evolve the simulation of the chain with no anchoring in a box of fixed size.
Same requirement of the previous one