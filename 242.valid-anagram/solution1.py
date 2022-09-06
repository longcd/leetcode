# Source : https://leetcode.cn/problems/valid-anagram/
# Author : longchangda
# Time   : 2022-09-06

"""
哈希表

思路及算法
从另一个角度考虑，t 是 s 的异位词等价于「两个字符串中字符出现的种类和次数均相等」。

由于字符串只包含 26 个小写字母，因此我们可以维护一个长度为 26 的频次数组 table，
先遍历记录字符串 s 中字符出现的频次，然后遍历字符串 t，减去 table 中对应的频次，
如果出现 table[i]<0，则说明 t 包含一个不在 s 中的额外字符，返回 false 即可。

Time Complexity: O(n)
Space Complexity: O(|S|)，S 是字符集，这道题中 S 为全部小写英语字母，因此 |S| = 26。
"""


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        cnt = [0] * 26
        for c in s:
            index = ord(c) - ord("a")
            cnt[index] += 1

        for c in t:
            index = ord(c) - ord("a")
            cnt[index] -= 1
            if cnt[index] < 0:
                return False

        return True
