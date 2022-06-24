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

        self.matrix = np.matrix(matrix)
    
