import numpy as np

N = 1000000

z = np.random.random(N)
x = z**2

def f(x):
    return 1/(1+np.exp(x))

I = sum(f(x))/N*2

print(I)