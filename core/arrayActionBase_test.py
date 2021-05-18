import unittest

from .arithmeticOperationBase import *
from .arrayActionBase import *
from .stringBase import *


class TestDirk(unittest.TestCase):

    def test_1(self):
        pass
        # arr = 数组(["a", "b", "c"])
        # arr.加入成员("a")
        arr = 数组()
        for i in range(10):
            arr.加入成员(取随机数(1, 100))

        print(arr.取所有成员())
        arr.排序(reverse=False)
        print(arr.取所有成员())
        arr.排序(reverse=True)
        print(arr.取所有成员())

        arr2 = 数组()
        print("arr2???",arr2.取所有成员())


        for i in range(10):
            arr2.加入成员((取随机数(1, 100), 字符(65 + i)))

        print(arr2.取所有成员())
        arr2.排序(reverse=False)
        print(arr2.取所有成员())
        # arr2.排序(reverse=True,)
        arr2.排序(reverse=True, key=lambda d: d[0])
        print(arr2.取所有成员())
