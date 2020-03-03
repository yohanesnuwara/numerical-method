#no 1

import numpy as np

x = np.array([1,2,3])
y = np.array([1,2,3])

def regresi(x, y):
    xy = x * y
    xsquare = x**2
    ysquare = y**2
    xy_sum = np.sum(xy)
    x_sum = np.sum(x)
    y_sum = np.sum(y)
    xsquare_sum = np.sum(xsquare)
    ysquare_sum = np.sum(ysquare)
    x_squared = x_sum**2
    y_squared = y_sum**2

    b = ((len(x) * xy_sum) - (x_sum * y_sum)) / ((len(x) * xsquare_sum) - x_squared)
    a = ((y_sum * xsquare_sum) - (x_sum * xy_sum)) / ((len(x) * x_squared) - x_squared)
    return(a, b)

hasil = regresi(x,y)
print(hasil)
