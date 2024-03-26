# -*- coding: UTF-8 -*-
# author:      Liu Kun
# email:       liukunup@outlook.com
# timestamp:   2024/3/17 11:08
# description: XXX

import pytest


def inc(x):
    return x + 1


@pytest.mark.parametrize("x, expected", [(1, 2), (1, 3), (8, 9)])
class TestInc:

    def test_inc(self, x, expected):
        print(f"\ntest inc x={x}, expected={expected}")
        assert inc(x) == expected
