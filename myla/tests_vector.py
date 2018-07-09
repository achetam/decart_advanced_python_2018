import myla.vector as vector
import unittest

# def test_vector_equality_unequal_length():
#     v1 = [1, 2, 3]
#     v2 = [1, 2]
#     unittest.assertRaises(vector.veq_eq(v1, v2), ValueError)


def test_vector_equality_1():
    v1 = [1, 2, 3]
    v2 = [1, 2, 3]

    assert vector.vec_eq(v1, v2)


def test_vector_equality_2():
    v1 = [1, 2, 3]
    v2 = [4, 5, 6]

    assert vector.vec_eq(v1, v2) == False
