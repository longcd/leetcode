# Source : https://leetcode.cn/problems/first-unique-character-in-a-string/
# Author : longchangda
# Time   : 2022-09-06

"""
使用哈希表存储频数

思路及算法
我们可以对字符串进行两次遍历。

在第一次遍历时，我们使用哈希映射统计出字符串中每个字符出现的次数。
在第二次遍历时，我们只要遍历到了一个只出现一次的字符，那么就返回它的索引，否则在遍历结束后返回 -1。

Time Complexity: O(n)
Space Complexity: O(∣Σ∣)，其中 Σ 是字符集，在本题中 s 只包含小写字母，因此 ∣Σ∣ ≤ 26。
"""


class Solution:
    def firstUniqChar(self, s: str) -> int:
        hash_table = [0] * 26
        for c in s:
            index = ord(c) - ord("a")
            hash_table[index] += 1

        for i, c in enumerate(s):
            index = ord(c) - ord("a")
            if hash_table[index] == 1:
                return i

        return -1
