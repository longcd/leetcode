# Source : https://leetcode.cn/problems/valid-anagram/
# Author : longchangda
# Time   : 2022-09-06

"""
排序

思路及算法
t 是 s 的异位词等价于「两个字符串排序后相等」。

因此我们可以对字符串 s 和 t 分别排序，看排序后的字符串是否相等即可判断。
此外，如果 s 和 t 的长度不同，t 必然不是 s 的异位词。

Time Complexity: O(nlogn)
Space Complexity: O(logn)
"""


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        str1 = "".join(sorted(s))
        str2 = "".join(sorted(t))

        return str1 == str2
