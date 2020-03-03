#soal no 3
#soal no 3

A = [[1, -1, 0, -1, 1], [0, 8/3, -1, -1/3, 1], [0, 0, 21/5, -7/8, 1], [0, 0, 0, 17/7, 1]]
# sistem persamaan untuk A =  [[1, -1, 0, -1], [0, 8/3, -1, -1/3], [0, 0, 21/5, -7/8], [0, 0, 0, 17/7]]
# dan B = [[1], [1], [1], [1]]
# lalu keduanya di-concatenate sehingga dibuat matriks non-uniform

def gauss(A):
    m = len(A)
    # matriks non-uniform
    assert all([len(row) == m + 1 for row in A[1:]])
    n = m + 1

    for k in range(m):
        pivots = [abs(A[i][k]) for i in range(k, m)]
        i_max = pivots.index(max(pivots)) + k

        # cek singularisasi dari matriks
        assert A[i_max][k] != 0

        # swapping row
        A[k], A[i_max] = A[i_max], A[k]

        for i in range(k + 1, m):
            f = A[i][k] / A[k][k]
            for j in range(k + 1, n):
                A[i][j] -= A[k][j] * f

            # isi matriks trinangular dengan nol
            A[i][k] = 0

    # Selesaikan persamaan
    x = []
    for i in range(m - 1, -1, -1):
        x.insert(0, A[i][m] / A[i][i])
        for k in range(i - 1, -1, -1):
            A[k][m] -= A[k][i] * x[0]
    return x

hasil = gauss(A)
print(hasil)