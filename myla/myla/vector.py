"""
Here are some vector functionsself.
"""
import math


def vec_eq(v1, v2):
    """
    This function checks whether two vectors are equal.
    Raises a value error if vectors are of unequal lengths.

    """
    if len(v1) != len(v2):
        raise ValueError("Vectors are of unequal lengths. Try again.")
    return(v1 == v2)


def alpha_x_v(alpha, v):
    """
    This function computes the scalar product of a vector

    alpha: scalar
    v: vector

    Returns: a vector
    """
    newvec = [x * alpha for x in v]
    return(newvec)


def v_plus_v(v1, v2):
    """
    This function adds two vectors.
    Raises value error if the vectors are of unequal lengths.

    inputs: vectors
    """
    if len(v1)==len(v2):
        return([x + y for x, y in zip(v1, v2)])
    else:
        raise ValueError("These vectors are of different lengths. Try again!")


def inner(v1,v2):
    """
    This function computes an inner product of two vectors.
    """
    if len(v1) != len(v2):
        raise ValueError("These vectors are of different lengths. Try again!")
    return sum([x*y for x, y in zip(v1, v2)])


def l2_norm(v):
    """
    This function computes an L2 norm of a vector.
    """
    return math.sqrt(sum([elem**2 for elem in v]))
