# Source : https://leetcode.cn/problems/pascals-triangle-ii/
# Author : longchangda
# Time   : 20220922

"""
线性递推

Time Complexity: O(rowIndex)
Space Complexity: O(1)
"""


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row = [1]
        for i in range(1, rowIndex + 1):
            row.append(int(row[i - 1] * (rowIndex - i + 1) / i))
        return row

