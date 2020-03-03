#soal 2

import numpy as np

x = 2
N = 10
def maclaurin(x, N):
    # x = input, N = orde
    x = np.radians(x)
    k = 0; hasil = 0; sign = 1

    while k<N:
        temp = sign*x**(k)/np.math.factorial(k)
        hasil = hasil + temp
        k += 2
        sign = -sign
    return(hasil)

cosx = maclaurin(x, N)
print(cosx)