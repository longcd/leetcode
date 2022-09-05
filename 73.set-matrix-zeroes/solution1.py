# Source : https://leetcode.cn/problems/set-matrix-zeroes/
# Author : longchangda
# Time   : 2022-09-05

"""
使用标记数组

思路及算法
我们可以用两个标记数组分别记录每一行和每一列是否有零出现。

具体地，我们首先遍历该数组一次，如果某个元素为 0，那么就将该元素所在的行和列所对应标记数组的位置置为 true。
最后我们再次遍历该数组，用标记数组更新原数组即可。

Time Complexity: O(m * n)
Space Complexity: O(m + n)
"""


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        row, col = [False] * m, [False] * n

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    row[i] = col[j] = True

        for i in range(m):
            for j in range(n):
                if row[i] or col[j]:
                    matrix[i][j] = 0
