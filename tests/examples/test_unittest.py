# -*- coding: UTF-8 -*-
# author:      Liu Kun
# email:       liukunup@outlook.com
# timestamp:   2024/3/17 11:07
# description: XXX

import unittest
from parameterized import parameterized, param


def inc(x):
    return x + 1


class TestInc(unittest.TestCase):

    def setUp(self):
        print("\n")
        print("TestInc setUp")

    def tearDown(self):
        print("TestInc tearDown")

    @parameterized.expand([
        param(1, 2),
        param(1, 3),
        param(8, 9)
    ])
    def test_inc(self, x, expected):
        print(f"test inc x={x}, expected={expected}")
        self.assertEqual(inc(x), expected)
