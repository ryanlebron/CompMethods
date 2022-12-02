import numpy as np
import matplotlib.pyplot as plt


def f(r, t, R, rho, m):
    g = 9.8
    C = 0.47
    x, y, vx, vy = r
    v = np.sqrt(vx ** 2 + vy ** 2)
    d = (np.pi * (R ** 2) * rho * C) * 0.5
    dvx = -d * vx * v / m
    dvy = (-d * vy * v / m) - g
    return(np.array([vx, vy, dvx, dvy]))


def rk4(f, r, R, rho, m, a, b, N=10000):
    h = (b - a) / N
    tpoints = np.linspace(a, b, N)
    sol = np.empty((len(tpoints), 4))
    for i, t in enumerate(tpoints):
        sol[i, :] = r
        k1 = h * f(r, t, R, rho, m)
        k2 = h * f(r + (0.5 * k1), t + (0.5 * h), R, rho, m)
        k3 = h * f(r + (0.5 * k2), t + (0.5 * h), R, rho, m)
        k4 = h * f(r + k3, t + h, R, rho, m)
        r += (k1 + (2 * k2) + (2 * k3) + k4) / 6
    return sol


rho = 1.22
R = 0.08
m = np.arange(1, 102, 20)
for i in m:
    r = np.array([0, 0, (100 * np.cos(30 * np.pi / 180)),
                  (100 * np.sin(30 * np.pi / 180))])
    z = rk4(f, r, R, rho, i, 0, 10)
    x = z[:, 0]
    y = [j for j in z[:, 1] if j > 0]
    plt.plot(x[:len(y)], y, label="{}kg".format(i))

g = -9.8
v = 100
theta = 30 * np.pi / 180
t = np.linspace(0, 11, 100)
x_0 = (v * np.cos(theta)) * t
y_0 = (v * np.sin(theta) * t) + (0.5 * g * t * t)
z_0 = [i for i in y_0 if i > 0]
plt.plot(x_0[:len(z_0)], z_0, color="k", label="No Air Resistance")
plt.xlabel("Horizontal Distance (m)")
plt.ylabel("Vertical Distance (m)")
plt.title("Projectile Motion of Different Mass Cannonball")
plt.legend(fontsize="small")
plt.show()
