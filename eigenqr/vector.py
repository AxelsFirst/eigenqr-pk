import numpy as np


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
        return Vector(np.outer(self.vector, other.vector))
