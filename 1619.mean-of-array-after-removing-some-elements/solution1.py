# Source : https://leetcode.cn/problems/mean-of-array-after-removing-some-elements/
# Author : longchangda
# Time   : 2022-09-14

"""
排序

设元素数目为 n，我们先对整数数组 arr 从小到大进行排序，
然后对区间 [n/20, 19n/20) 内的元素进行求和，得到未删除元素的求和结果 partialSum，
返回均值 partialSum / 0.9n

Time Complexity: O(NlogN)
Space Complexity: O(logN)
"""


class Solution:
    def trimMean(self, arr: List[int]) -> float:
        arr.sort()
        n = len(arr)
        return sum(arr[n // 20 : 19 * n // 20]) / (n * 0.9)
