# Source : https://leetcode.cn/problems/reshape-the-matrix/
# Author : longchangda
# Time   : 2022-09-04

"""
Time Complexity: O(rc)
Space Complexity: O(1)
"""


class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        if m * n != r * c:
            return mat

        ans = [[0 for _ in range(c)] for _ in range(r)]
        i, j = 0, 0
        for row in mat:
            for col in row:
                ans[i][j] = col
                j += 1
                if j == c:
                    i += 1
                    j = 0

        return ans
