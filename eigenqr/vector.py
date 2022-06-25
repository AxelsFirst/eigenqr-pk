import numpy as np
from matrix import Matrix

class Vector(object):
    """

    Representation of vectors.

    """
    def __init__(self, vector):
        """

        Parameters:
        -----------
        Vector: a one dimensional array.

        """

        self.vector = np.array(vector)

    def __mul__(self, other):
        """

        Multiplication of vectors

        Parameters:
        -----------
        other: an instance of a Vector class.

        """
        return Matrix(np.outer(self.vector, other.vector))

    def norm(self):
        """

        Norm of the vector

        """
        return np.linalg.norm(self.vector)