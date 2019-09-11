from base import TestClass


def inc(x):
    return TestClass.inc(x)


def test_answer():
    x = [1]
    test_class = inc(x)

    assert x[0] == 2 and isinstance(test_class, TestClass)
