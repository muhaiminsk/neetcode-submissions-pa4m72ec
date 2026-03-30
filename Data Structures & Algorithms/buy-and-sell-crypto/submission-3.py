class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        money = 0

        for r in range(len(prices)):
            if prices[r]<prices[l]:
                l=r
            money = max(money, prices[r]-prices[l])
        return money
        