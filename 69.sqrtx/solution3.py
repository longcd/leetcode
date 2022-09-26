# Source : https://leetcode.cn/problems/sqrtx/
# Author : longcd
# Time   : 2022-09-26

"""
牛顿迭代法

Time Complexity: O(logx)
Space Complexity: O(1)
"""


class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0

        C, x0 = x, x
        while True:
            xi = 0.5 * (x0 + C / x0)
            if abs(x0 - xi) < 1e-7:
                break
            x0 = xi

        return int(x0)
