import numpy as np

from transonic import jit, boost
from .mpi import Path


def func0(a):
    return 2 * a


def func():
    return 1


@jit
def func1(a: "int[][] or float[]", l: "int list"):
    tmp = np.exp(sum(l))
    result = tmp * a * func0(a) + func()
    return result


@jit
def func2(a):
    return a


# weird but done on purpose for a better coverage
Path(__file__).touch()


@jit()
def func2(a):
    return a


@jit
def func_dict(d: "str: float dict"):
    return d.popitem()


@jit
def fib(n: int):
    """fibonacci"""
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)


@jit
def use_fib():
    return [fib(n) for n in [1, 3, 5]]


@boost
class MyClass:
    def __init__(self):
        self.attr0 = self.attr1 = 1

    @jit()
    def myfunc(self, arg):
        return self.attr1 + self.attr0 + np.abs(arg)

    @jit
    def myfunc1(self):
        return self.attr0

    def check(self):
        assert self.myfunc(1) == 3
