# Source : https://leetcode.cn/problems/sqrtx/
# Author : longcd
# Time   : 2022-09-26

"""
二分查找
x 平方根的整数部分 ans 是满足 i^2 <= x 的最大 i 值

Time Complexity: O(logx)
Space Complexity: O(1)
"""


class Solution:
    def mySqrt(self, x: int) -> int:
        l, r, ans = 0, x, -1
        while l <= r:
            mid = l + (r - l) // 2
            if mid * mid <= x:
                ans = mid
                l = mid + 1
            else:
                r = mid - 1
        return ans
