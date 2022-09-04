# Source : https://leetcode.cn/problems/reshape-the-matrix/
# Author : longchangda
# Time   : 2022-09-04

"""
二维数组的一维表示

Time Complexity: O(rc)
Space Complexity: O(1)
"""


class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        if m * n != r * c:
            return mat

        ans = [[0 for _ in range(c)] for _ in range(r)]
        for x in range(m * n):
            ans[x // c][x % c] = mat[x // n][x % n]

        return ans
