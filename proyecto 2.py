import numpy as np
import os

def Lectura():
    global x
    global y
    x = int(input("ingrese el numero de columnas(x) de la matriz"))
    y = int(input("ingrese el numero de filas(y) de la matriz"))
    MatO = np.zeros((y, x))   #en numpy los array se manejan con y, x siendo la primera columna 0

    for i in range(y):
        for j in range(x):
            MatO[i, j] = int(input(f"ingrese el valor en la posicision [{j+1},{i+1}]"))
    print(MatO)
    return MatO


def SepColumn(mat):
    vect1 = []
    for i in range(x):
        vect1.append(mat[i, :])
    vec = np.array(vect1)
    print(vec)
    return vec


def gram_schmidt(A):
    n = A.shape[1]#numero de vectores
    for j in range(n):
        # To orthogonalize the vector in column j with respect to the
        # previous vectors, subtract from it its projection onto
        # each of the previous vectors.
        for k in range(j):
            A[:, j] -= np.dot(A[:, k], A[:, j]) * A[:, k]
        A[:, j] = A[:, j] / np.linalg.norm(A[:, j])
    return A

if __name__ == '__main__':  # función main
    mat = Lectura()
    vec = SepColumn(mat)
    print(gram_schmidt(vec))

