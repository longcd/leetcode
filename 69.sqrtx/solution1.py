# Source : https://leetcode.cn/problems/sqrtx/
# Author : longcd
# Time   : 2022-09-26

"""
暴力解法
x 平方根的整数部分 ans 是满足 i^2 <= x 的最大 i 值

Time Complexity: O(x)
Space Complexity: O(1)
"""


class Solution:
    def mySqrt(self, x: int) -> int:
        ans = 0
        for i in range(x + 1):
            if i * i <= x:
                ans = i
            else:
                break
        return ans
