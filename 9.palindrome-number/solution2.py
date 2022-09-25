# Source : https://leetcode.cn/problems/palindrome-number/
# Author : longcd
# Time   : 2022-09-25

"""
反转一半数字

Time Complexity: O(logn)
Space Complexity: O(1)
"""


class Solution:
    def isPalindrome(self, x: int) -> bool:
        # 特殊情况：
        # 当 x < 0 时，x 不是回文数。
        # 同样地，如果数字的最后一位是 0，为了使该数字为回文，
        # 则其第一位数字也应该是 0，只有 0 满足这一属性
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        reverted_number = 0
        while x > reverted_number:
            reverted_number = reverted_number * 10 + x % 10
            x //= 10

        # 当数字长度为奇数时，我们可以通过 reverted_number // 10 去除处于中位的数字
        # 由于处于中位的数字不影响回文，所以我们可以简单地将其去除
        return x == reverted_number or x == reverted_number // 10
