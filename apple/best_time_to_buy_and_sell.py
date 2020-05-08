import sys
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        max_profit_so_far = 0
        min_price_so_far = sys.maxsize

        for i in range(len(prices)):

            if prices[i] > min_price_so_far:
                max_profit_so_far = max(max_profit_so_far, prices[i] - min_price_so_far)

            if prices[i] < min_price_so_far:
                min_price_so_far = prices[i]

        return max_profit_so_far



assert Solution().maxProfit([7,1,5,3,6,4]) == 5
assert Solution().maxProfit([7,6,4,3,1]) == 0



