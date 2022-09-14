import numpy as np
import matplotlib.pyplot as plt

#part a
theta = np.linspace(0,2*np.pi,1000)
deltoidx = (2*np.cos(theta)) + (np.cos(2*theta))
deltoidy = (2*np.sin(theta)) - (np.sin(2*theta))


#part b
phi = np.linspace(0,10*np.pi,1000)
galileanr = phi**2
galileanx = galileanr*np.cos(phi)
galileany = galileanr*np.sin(phi)


#part c
psi = np.linspace(0,24*np.pi,1000)
feyr = (np.exp(np.cos(psi))) - (2*(np.cos(4*psi))) + ((np.sin(psi/12))**5)
feyx = feyr*np.cos(psi)
feyy = feyr*np.sin(psi)


#plotting
fig,axis=plt.subplots(nrows=1,ncols=3,figsize=(12,4))
axis[0].scatter(deltoidx,deltoidy)
axis[0].set_title("Deltoid Curve")
axis[1].scatter(galileanx,galileany)
axis[1].set_title("Galilean Spiral")
axis[2].scatter(feyx,feyy)
axis[2].set_title("Fey's Function")

plt.show()