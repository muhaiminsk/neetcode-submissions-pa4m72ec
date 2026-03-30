class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_ones = 0
        temp = 0

        for i in range(len(nums)):
            if nums[i] == 1:
                temp += 1
                max_ones = max(max_ones, temp)
            else:
                temp = 0
        return max_ones
        