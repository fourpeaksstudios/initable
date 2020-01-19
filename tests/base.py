from typing import List

from initable import initializable


class TestClass(object):
    """docstring for TestClass."""

    @initializable
    def inc(self, num: List):
        num[0] = num[0] + 1
