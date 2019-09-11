from typing import List

from base import TestClass


def inc(test_class: TestClass, x: List) -> TestClass:
    return test_class.inc(x)


def test_answer():
    x = [1]
    test_class = TestClass()

    inc(test_class, x)

    assert x[0] == 2
