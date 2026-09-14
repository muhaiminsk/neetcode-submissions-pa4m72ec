class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        maxPro = 0

        for r in range(1, len(prices)):
            maxPro = max(maxPro, (prices[r] - prices[l]))
            if prices[l]>prices[r]:
                l = r
        return maxPro

        