import numpy as np
import eigenqr.vector as ve


class Matrix(object):
    """

    Representation of matrices.

    """

    def __init__(self, matrix):
        """

        Parameters:
        -----------
        matrix: a two dimensional array.

        """

        self.matrix = np.array(matrix)

    def __add__(self, other):
        """

        Addition of matrices

        Parameters:
        -----------
        other: an instance of a Matrix class.

        """
        return Matrix(np.add(self.matrix, other.matrix))

    def __sub__(self, other):
        """

        Subtraction of matrices

        Parameters:
        -----------
        other: an instance of a Matrix class.

        """
        return Matrix(np.subtract(self.matrix, other.matrix))

    def __mul__(self, other):
        """

        Multiplication of matrices

        Parameters:
        -----------
        other: an instance of a Matrix class.

        """
        return Matrix(np.matmul(self.matrix, other.matrix))

    def qr_decomposition(self):
        """

        Calculates QR decomposition of a matrix

        Output:
        -------
        Q: an instance of a Matrix class
            Q is orthogonal

        R: an instance of a Matrix class
            R is upper triangular

        """

        QR = np.linalg.qr(self.matrix)

        Q = Matrix(QR[0])
        R = Matrix(QR[1])

        return Q, R

    def direct_sum(self, other):
        """

        Direct addition of matrices

        Parameters:
        -----------
        other: an instance of a Matrix class.

        """

        direct_sum = np.zeros(np.add(self.matrix.shape,
                              other.matrix.shape), dtype=int)

        direct_sum[:self.matrix.shape[0], :self.matrix.shape[1]] = self.matrix
        direct_sum[self.matrix.shape[0]:, self.matrix.shape[1]:] = other.matrix

        return direct_sum

    # def hessenberg_form(self):
    #     A = self
    #     n = 2
    #     H = A
    #     for i in range(1, n-2):
    """
    #         # compute u_i using x = [A[i+1,i], ..., A[n, i]]
    #         # compute P_i * A
    #         # compute P_i * A * P*_i
    """
    #         x = zero_vector(n-i)
    #         for k in range(i+1, n+1):
    #             x[k] = A[k, i]
    #         H = P_i() * H
    #         H = H * P_i() ?
    #     #H = P_k A P*_k
    #     return H


def identity_matrix(n):
    """

    Create identity Matrix

    Parameters:
    -----------
    n: an integer.

    Output:
    -------
    I_n: an instance of a Matrix class.

    """

    return Matrix(np.identity(n))


def householder_reflector(x):
    """

    Create a Householder reflector

    Parameters:
    -----------
    x: an instance of a Vector class.

    Output:
    -------
    P: an instance of a Matrix class.

    """

    n = len(x)
    I_n = identity_matrix(n)
    u = ve.householder_vector(x)

    P = I_n - 2 * (u * u)

    return P


def householder_application(A, x, i):
    """

    Create a Householder reflector

    Parameters:
    -----------
    A: an instance of a Matrix class.
    x: an instance of a Vector class.
    i: an integer.

    Output:
    -------
    P_i: an instance of a Matrix class.

    """

    n = len(A.matrix)
    I_n = identity_matrix(n-i)
    P = householder_reflector(x)

    P_i = I_n.direct_sum(P)

    return P_i
