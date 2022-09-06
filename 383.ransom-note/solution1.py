# Source : https://leetcode.cn/problems/ransom-note/
# Author : longchangda
# Time   : 2022-09-06

"""
字符统计

思路及算法
按照题目要求，只需要满足字符串 magazine 中的每个英文字母 ('a'-'z') 的统计次数都大于等于 ransomNote 中相同字母的统计次数即可。

如果字符串 magazine 的长度小于字符串 ransomNote 的长度，则我们可以肯定 magazine 无法构成 ransomNote，此时直接返回 false。

Time Complexity: O(m + n)
Space Complexity: O(|S|)，S 是字符集，这道题中 S 为全部小写英语字母，因此 |S| = 26。
"""


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False

        cnt = [0] * 26
        for c in magazine:
            index = ord(c) - ord("a")
            cnt[index] += 1

        for c in ransomNote:
            index = ord(c) - ord("a")
            cnt[index] -= 1
            if cnt[index] < 0:
                return False

        return True
