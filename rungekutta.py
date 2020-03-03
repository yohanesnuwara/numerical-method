import numpy as np

# input fungsi ODE yang diinginkan
def dydx(x, y): 
    # return (1 + y**2)
    return((0.7*y*(1-(y/750)))-20)

def rungekutta(x0, y0, x, h):
    # step height h 
    n = np.int((x - x0) / h)
    # iterasi
    y = y0
    for i in range(1, n + 1):
        
        # formulasi runge-kutta 4th order
        k1 = h * dydx(x0, y)
        k2 = h * dydx(x0 + 0.5 * h, y + 0.5 * k1)
        k3 = h * dydx(x0 + 0.5 * h, y + 0.5 * k2)
        k4 = h * dydx(x0 + h, y + k3)
        y = y + (1.0 / 6.0) * (k1 + 2 * k2 + 2 * k3 + k4)

        x0 = x0 + h
    return y

# input nilai yang diinginkan
x0 = 0
y0 = 30
x = 100
h = 0.1
hasil = rungekutta(x0, y0, x, h)
print(hasil)
