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
