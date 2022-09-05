# Source : https://leetcode.cn/problems/valid-sudoku/
# Author : longchangda
# Time   : 2022-09-05

"""
一次遍历

思路及算法
可以使用哈希表记录每一行、每一列和每一个小九宫格中，每个数字出现的次数。
只需要遍历数独一次，在遍历的过程中更新哈希表中的计数，并判断是否满足有效的数独的条件即可。

由于数独中的数字范围是 1 到 9，因此可以使用数组代替哈希表进行计数。

Time Complexity: O(1)
Space Complexity: O(1)
"""


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [[0 for _ in range(9)] for _ in range(9)]
        columns = [[0 for _ in range(9)] for _ in range(9)]
        subboxes = [[[0 for _ in range(9)] for _ in range(3)] for _ in range(3)]

        for i in range(9):
            for j in range(9):
                c = board[i][j]
                if c != ".":
                    index = ord(c) - ord("1")
                    rows[i][index] += 1
                    columns[j][index] += 1
                    subboxes[i // 3][j // 3][index] += 1
                    if (
                        rows[i][index] > 1
                        or columns[j][index] > 1
                        or subboxes[i // 3][j // 3][index] > 1
                    ):
                        return False

        return True
