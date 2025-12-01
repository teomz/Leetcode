class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        max = 0

        for i in range(len(prices)):
            if min_price < prices[i]:
                max += (prices[i] - min_price)
            
            min_price = prices[i]

        return max