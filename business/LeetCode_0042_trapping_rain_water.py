#!/usr/bin/python
# -*- coding: utf-8 -*-
# author:    LiuKun
# timestamp: 2022-11-28 23:39:38

# 导入所需的依赖库
import unittest
from typing import List


# 请完成以下开发代码(如不符合语法要求,自行修改即可)
class Solution:

    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        n = len(height)

        left_max = [height[0]] + [0] * (n - 1)
        for i in range(1, n):
            left_max[i] = max(left_max[i - 1], height[i])

        right_max = [0] * (n - 1) + [height[n-1]]
        for i in range(n - 2, -1, -1):
            right_max[i] = max(right_max[i + 1], height[i])

        return sum( min(left_max[i], right_max[i]) - height[i] for i in range(n) )

    def trap_v2(self, height: List[int]) -> int:
        stack = list()
        ans = 0
        for i, h in enumerate(height):
            while stack and h > height[stack[-1]]:
                top = stack.pop()
                if not stack:
                    break
                left = stack[-1]
                cur_w = i - left - 1
                cut_h = min(height[left], h) - height[top]
                ans += cur_w * cut_h
            stack.append(i)
        return ans

    def trap_v3(self, height: List[int]) -> int:
        ans = 0
        left, right = 0, len(height) - 1
        left_max, right_max = 0, 0
        while left < right:
            left_max = max(left_max, height[left])
            right_max = max(right_max, height[right])
            if height[left] < height[right]:
                ans += left_max - height[left]
                left += 1
            else:
                ans += right_max - height[right]
                right -= 1
        return ans


# 请完成以下测试代码
class SolutionTest(unittest.TestCase):

    def setUp(self):
        # 实例化
        self.inst = Solution()

    def tearDown(self):
        pass

    # 请设计一些测试用例来验证
    def test_case_1(self):
        self.assertEqual(self.inst.trap(height=[0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]), 6)

    def test_case_2(self):
        self.assertEqual(self.inst.trap(height=[4, 2, 0, 3, 2, 5]), 9)


if __name__ == "__main__":
    unittest.main()
