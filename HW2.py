import numpy as np
import matplotlib.pyplot as plt


#function for trapizoidal integration
def trapint(a,b,N):
    #defining the function to integrate
    def f(x):
        return np.exp(-x**2)
    dx = (b-a)/N
    F = (.5*f(a)) + (.5*f(b))
    for k in range(1,N):
        F = F + f(a+(k*dx))
    return(dx*F)

print(trapint(0.0,3.0,30))

#plotting
x = np.linspace(0,3,100)
y = trapint(0,x,30)

plt.plot(x,y,linestyle='solid')
plt.title(r"Integral of $e^{-t^{2}}$")
plt.xticks()
plt.yticks()
plt.grid(linestyle='--')
plt.show()
