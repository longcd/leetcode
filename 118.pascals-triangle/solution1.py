# Source : https://leetcode.cn/problems/pascals-triangle/
# Author : longchangda
# Time   : 2022-09-04


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = list()
        for i in range(numRows):
            row = list()
            for j in range(i + 1):
                if j == 0 or j == i:
                    row.append(1)
                else:
                    row.append(ans[i - 1][j - 1] + ans[i - 1][j])
            ans.append(row)

        return ans
