# Source : https://leetcode.cn/problems/first-unique-character-in-a-string/
# Author : longchangda
# Time   : 2022-09-06

"""
使用哈希表存储索引

思路及算法
具体地，对于哈希映射中的每一个键值对，键表示一个字符，值表示它的首次出现的索引（如果该字符只出现一次）或者 -1（如果该字符出现多次）。
当我们第一次遍历字符串时，设当前遍历到的字符为 c，
如果 c 不在哈希映射中，我们就将 c 与它的索引作为一个键值对加入哈希映射中，
否则我们将 c 在哈希映射中对应的值修改为 -1。

在第一次遍历结束后，我们只需要再遍历一次哈希映射中的所有值，找出其中不为 -1 的最小值，
即为第一个不重复字符的索引。如果哈希映射中的所有值均为 -1，我们就返回 -1。

Time Complexity: O(n)
Space Complexity: O(∣Σ∣)，其中 Σ 是字符集，在本题中 s 只包含小写字母，因此 ∣Σ∣ ≤ 26。
"""


class Solution:
    def firstUniqChar(self, s: str) -> int:
        position = dict()
        n = len(s)
        for i, c in enumerate(s):
            if c in position:
                position[c] = -1
            else:
                position[c] = i

        first = n
        for pos in position.values():
            if pos != -1 and pos < first:
                first = pos
        if first == n:
            return -1
        return first
