import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle

#function for electric potential
def electric_potential(q,r0,x,y):
    distance = np.hypot(x-r0[0],y-r0[1])
    denominator = 4*np.pi*8.854e-12*distance
    phi = q/denominator
    return phi

#1m x 1m sqaure plane spaced by 1cm
X, Y = np.meshgrid(np.linspace(-50,50,100),np.linspace(-50,50,100))

#create list with our two charges in it
charges = [(-1,(4.9,0)),(1,(-5.1,0))]

V = np.zeros((100,100))

#electric potential at all points
for charge in charges:
    ev = electric_potential(*charge, x=X , y=Y)
    V += ev

#electric field = gradient of electric potential
# for E in charges:
#     h = 1e-5
#     Ex = electric_potential(*E, x=(((X+h/2)-(X-h/2))/2),y=Y)
#     Ey = electric_potential(*E,x=X,y=(((Y+h/2)-(Y-h/2))/2))

#could not get the plot to look right with this method 
#so used np.gradient 

Ey, Ex = np.gradient(V, np.linspace(-50,50,100), np.linspace(-50,50,100) )

#plotting 
fig,ax=plt.subplots(nrows=1,ncols=2,figsize=(12,4))

#electric potential
plt.colorbar(ax[0].contourf(X,Y,V,20,cmap='inferno'),ax=ax[0])
ax[0].set_title("Electric Potential Due to Point Charges")
ax[0].set_xlim(-15,15)
ax[0].set_ylim(-15,15)
ax[0].set_xlabel("X distance (cm)")
ax[0].set_ylabel("Y distance (cm)")

#electric field
field_strength = np.log(np.hypot(Ex,Ey))
ax[1].streamplot(X,Y,Ex,Ey,color=field_strength,cmap='inferno')

ax[1].set_title("Electric Field Due to Point Charges")
ax[1].set_xlabel("X distance (cm)")
ax[1].set_ylabel("Y distance (cm)")

#add the charges themselves to the plot
charge_colors = {True:'red',False:'blue'} #going to pass q>0 so that postive and negative charges are either red or blue
for q,pos in charges:
    ax[1].add_artist(Circle(pos,1,color=charge_colors[q>0]))


plt.show()
