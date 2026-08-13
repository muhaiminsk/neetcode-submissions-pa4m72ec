class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        maxP=0

        for r in range(len(prices)):
            p = prices[r] - prices[l]
            maxP = max(maxP, p)

            if prices[r]<prices[l]:
                l=r
        return maxP
        