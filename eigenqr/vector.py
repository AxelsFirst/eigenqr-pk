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

        Outer product of vectors

        Parameters:
        -----------
        other: an instance of a Vector class.

        Output:
        -------
        M: an instance of a Matrix class.

        """

        from eigenqr.matrix import Matrix

        return Matrix(np.outer(self.vector, other.vector))

    def norm(self):
        """

        Calculate norm of a vector

        Output:
        -------
        norm: an integer.

        """

        return np.linalg.norm(self.vector)

    def normalization(self):
        """

        Get a normalized vector

        Output:
        -------
        normalized_vector: an instance of a Vector class.

        """

        is_all_zero = np.all((self.vector == 0))
        if is_all_zero:
            return self
        else:
            return Vector(self.vector/np.linalg.norm(self.vector))


def unit_vector(n):
    """

    Get a unit vector

    Output:
    -------
    e1: an instance of a Vector class.

    """

    e1 = np.zeros((n, ))
    e1[0] = 1

    return e1


def zero_vector(n):
    """

    Get a zero vector

    Parameters:
    -----------
    n: an integer.

    Output:
    -------
    v0: an instance of a Vector class.

    """

    return np.array(np.zeros((n,)))
