# Source : https://leetcode.cn/problems/summary-ranges/
# Author : longchangda
# Time   : 2022-09-23

"""
一次遍历

Time Complexity: O(n)
Space Complexity: O(1)
"""


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ret = list()
        i, n =0, len(nums)
        while i < n:
            low = i
            i += 1
            while i < n and nums[i] == nums[i-1] + 1:
                i += 1
            high = i - 1

            if low < high:
                temp = f"{nums[low]}->{nums[high]}"
            else:
                temp = str(nums[low])
            ret.append(temp)

        return ret

