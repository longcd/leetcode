# Source : https://leetcode.cn/problems/best-time-to-buy-and-sell-stock/
# Author : longchangda
# Time   : 2022-09-03

"""
一次遍历

思路及算法
我们只需要遍历价格数组一遍，记录历史最低点，
然后在每一天考虑这么一个问题：如果我是在历史最低点买进的，那么我今天卖出能赚多少钱？
当考虑完所有天数之时，我们就得到了最好的答案。

Time Complexity: O(n)
Space Complexity: O(1)
"""


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_price = int(1e9)
        for price in prices:
            max_profit = max(price - min_price, max_profit)
            min_price = min(price, min_price)

        return max_profit
