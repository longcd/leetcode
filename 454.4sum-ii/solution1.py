# Source : https://leetcode.cn/problems/4sum-ii/
# Author : longchangda
# Time   : 2022-09-14

"""
分组 + 哈希表

思路与算法

我们可以将四个数组分成两部分，A 和 B 为一组，C 和 D 为另外一组。

对于 A 和 B，我们使用二重循环对它们进行遍历，得到所有 A[i]+B[j] 的值并存入哈希映射中。对于哈希映射中的每个键值对，每个键表示一种 A[i]+B[j]，对应的值为 A[i]+B[j] 出现的次数。

对于 C 和 D，我们同样使用二重循环对它们进行遍历。当遍历到 C[k]+D[l] 时，如果 -(C[k]+D[l]) 出现在哈希映射中，那么将 -(C[k]+D[l]) 对应的值累加进答案中。

最终即可得到满足 A[i]+B[j]+C[k]+D[l]=0 的四元组数目。

Time Complexity: O(N^2)
Space Complexity: O(N^2)
"""


class Solution:
    def fourSumCount(
        self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]
    ) -> int:
        cnt = 0
        hashmap = dict()
        for i in nums1:
            for j in nums2:
                hashmap[i + j] = hashmap.get(i + j, 0) + 1

        for i in nums3:
            for j in nums4:
                cnt += hashmap.get(-1 * (i + j), 0)

        return cnt
