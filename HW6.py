from vpython import sphere,rate,vector
from random import randint
import numpy as np


#start L at 101
L = 101

#values so the particle is in the middle of the grid
i = 50
j = 50

#create the point and set its position
particle = sphere(make_trail=True)
particle.p= vector(i,j,0)


#main loop
for t in np.arange(1e6):
    rate(45) #specify speed
    particle.pos = vector(i-50,j-50,0)
    a = randint(1,4) #random number for four random directions
    if a == 1: #move up
        if i == L: #check for edges
            continue
        i += 1
    elif a == 2: #etc
        if i == 0:
            continue
        i -= 1
    elif a == 3:
        if j == L:
            continue
        j += 1
    elif a == 4:
        if j == 0:
            continue
        j -= 1
