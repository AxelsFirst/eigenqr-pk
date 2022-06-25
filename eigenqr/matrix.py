import numpy as np


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

    def householder_application(self, x, i):
        """

        Create a Householder reflector

        Parameters:
        -----------
        x: an instance of a Vector class.
        i: an integer.

        Output:
        -------
        P_i: an instance of a Matrix class.

        """

        n = len(self.matrix)
        I_n = identity_matrix(n-i)
        P = x.householder_reflector()

        P_i = I_n.direct_sum(P)

        return P_i

    def hessenberg_form(self):
        """

        Create a Hessenberg form of a matrix

        Output:
        -------
        H: an instance of a Matrix class.

        """

        from eigenqr.vector import zero_vector
        from copy import deepcopy

        n = 2
        H = deepcopy(self)

        for i in range(1, n-2):
            x = zero_vector(n-i)

            for k in range(i+1, n+1):
                x[k] = H.matrix[k, i]

            H = H.householder_application(x, i) * H
            H = H * H.householder_application(x, i)

        return H


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
