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
    
        def direct_sum(self,other):
        """

        Direct addition of matrices

        Parameters:
        -----------
        other: an instance of a Matrix class.

        """

        direct_sum = np.zeros(np.add(self.matrix.shape,other.matrix.shape), dtype=int)

        direct_sum[:self.matrix.shape[0],:self.matrix.shape[1]]=self.matrix
        direct_sum[self.matrix.shape[0]:,self.matrix.shape[1]:]=other.matrix
        
        return direct_sum
