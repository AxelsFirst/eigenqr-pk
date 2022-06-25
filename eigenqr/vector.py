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
            return self.vector
        else:
            return self.vector/np.linalg.norm(self.vector)

    def householder_vector(self):
        """

        Get a vector used in Householder reduction

        Output:
        -------
        u: an instance of a Vector class.

        """

        n = len(self.vector)
        norm_of_self = self.norm()
        rho = np.sign(self.vector[0])
        e1 = unit_vector(n)

        if rho == 0:
            rho = 1

        alpha = rho * norm_of_self

        z = self.vector - alpha * e1
        u = z.normalization()

        return u

    def householder_reflector(self):
        """

        Create a Householder reflector

        Parameters:
        -----------
        x: an instance of a Vector class.

        Output:
        -------
        P: an instance of a Matrix class.

        """

        from eigenqr.matrix import identity_matrix

        n = len(self.vector)
        I_n = identity_matrix(n)
        u = self.householder_vector()

        P = I_n - 2 * (u * u)

        return P


def unit_vector(n):
    """

    Get a unit vector

    Output:
    -------
    e1: an instance of a Vector class.

    """

    e1 = np.zeros((1, n))
    e1[0, 0] = 1

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

    return np.array(np.zeros((n,), dtype=int))
