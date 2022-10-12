# Constants
G = 6.674e-11
M_earth = 5.974e24
m = 7.348e22
R = 3.844e8
omega = 2.662e-6

#orbital equation
def func(r):
    return (G*M_earth/r**2) - (G*m/(R-r)**2) - (omega**2)*r

#derivative of orbital equation
def derivative(r):
    return (-2*G*M_earth/r**3) - (2*G*m/(R-r)**3) - (omega**2)

#Initial guess
r = R/2

#cap on how many times we iterate
max_iterations = 100

err = 1e-5

#Newton's method
for iteration in range(max_iterations+1):
    #calculate delta_r
    delta_r = -func(r)/derivative(r)
    r = r + delta_r

if iteration <= max_iterations:
    print(r)
    print('The distance from the center of the earth to L1 is r =',r,'m')
