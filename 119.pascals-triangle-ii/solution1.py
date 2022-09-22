# Source : https://leetcode.cn/problems/pascals-triangle-ii/
# Author : longchangda
# Time   : 20220922

"""
递推

Time Complexity: O(rowIndex^2)
Space Complexity: O(1)
"""


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        pre = list()
        for i in range(rowIndex + 1):
            cur = list()
            for j in range(i + 1):
                if j == 0 or j == i:
                    cur.append(1)
                else:
                    cur.append(pre[j - 1] + pre[j])
            pre = cur
        return pre

