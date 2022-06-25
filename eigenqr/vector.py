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

    def normalization(self):
        """

        normalization of the vector

        """
        is_all_zero = np.all((self.vector == 0))
        if is_all_zero:
          return self.vector
        else:
          return self.vector/np.linalg.norm(self.vector)


def unit_vector(size):
  return np.array([1,np.zeros((size-1,), dtype=int)])
unit_vector(5)
