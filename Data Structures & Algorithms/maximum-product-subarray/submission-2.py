class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        curMax, curMin = 1, 1


        for n in nums:
            tmp = curMax
            curMax, curMin = max(n*curMax, n*curMin, n), min(n*tmp, n*curMin, n)
            #curMin = min(n*tmp, n*curMin, n)
            res = max(res, curMax)

        return res