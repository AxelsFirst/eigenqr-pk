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

        Outer product of vectors

        Parameters:
        -----------
        other: an instance of a Vector class.

        Output:
        -------
        M: an instance of a Matrix class.

        """

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
            return self.vector
        else:
            return self.vector/np.linalg.norm(self.vector)


def unit_vector(size):
    """

    Get a unit vector

    Output:
    -------
    e1: an instance of a Vector class.

    """

    return np.array([1, np.zeros((size-1,), dtype=int)])


def householder_vector(x):
    """

    Get a vector used in Householder reduction

    Output:
    -------
    u: an instance of a Vector class.

    """

    n = len(x)
    norm_of_x = x.norm()
    rho = np.sign(x[0])
    e1 = unit_vector(n)

    if rho == 0:
        rho = 1

    alpha = rho * norm_of_x

    z = x - alpha * e1
    u = z.normalization()

    return u
