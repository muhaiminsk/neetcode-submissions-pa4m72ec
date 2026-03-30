class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = {0:1}
        curSum, total = 0, 0


        for i in nums:
            curSum += i
            diff = curSum - k
            total += prefix.get(diff, 0)
            prefix[curSum] = 1 + prefix.get(curSum, 0)

        return total
        