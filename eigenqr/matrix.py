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

        if type(other) == int:
            return Matrix(np.multiply(self.matrix, other))
        else:
            return Matrix(np.matmul(self.matrix, other.matrix))

    def get_shape(self):
        """

        Get the dimnensions of a matrix

        Output:
        -------
        shape: a list.

        """

        return self.matrix.shape

    def get_num_rows(self):
        """

        Get the vertical dimension of a matrix

        Output:
        -------
        num_rows: an integer.

        """

        return self.get_shape()[0]

    def get_num_cols(self):
        """

        Get the horizontal dimension of a matrix

        Output:
        -------
        num_cols: an integer.

        """

        return self.get_shape()[1]

    def check_square(self):
        """

        Check whether matrix is a square matrix

        Output:
        -------
        is_square: a boolean.

        """

        return self.get_num_rows() == self.get_num_cols()

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

    def qr_algorithm(self, n_max, eps):
        """

        Calculates eigenvalues of a matrix using the QR algorithm

        Parameters:
        -----------
        n_max: an integer.
        eps: a float.

        Output:
        -------
        eigenvalues: a list.

        """

        from scipy import linalg as la

        H = Matrix(la.hessenberg(self.matrix))
        n = H.matrix.shape[0]

        for i in range(n_max):
            Q, R = H.qr_decomposition()
            H = R * Q

        eigenvalues = []

        i = 0
        while i < n:
            if i == n-1:
                eigenvalues.append(H.matrix[i, i])

            elif abs(H.matrix[i+1, i]) < eps:
                eigenvalues.append(H.matrix[i, i])

            else:
                a = H.matrix[i, i]
                b = H.matrix[i, i+1]
                c = H.matrix[i+1, i]
                d = H.matrix[i+1, i+1]
                B = -1*(a+d)
                C = a*d - b*c
                eigen_plus = (-B + np.sqrt(B**2 - 4*C))/2
                eigen_minus = (-B - np.sqrt(B**2 - 4*C))/2

                eigenvalues.append(eigen_plus)
                eigenvalues.append(eigen_minus)

                i += 1
            i += 1

        return eigenvalues
