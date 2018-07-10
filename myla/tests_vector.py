import myla.vector as vector


def test_vector_equality_1():
    v1 = [1, 2, 3]
    v2 = [1, 2, 3]

    assert vector.vec_eq(v1, v2)


def test_vector_equality_2():
    v1 = [1, 2, 3]
    v2 = [4, 5, 6]

    with pytest.raises(ValueError):
        vec_eq(v1, v2)

    assert vector.vec_eq(v1, v2) == False
