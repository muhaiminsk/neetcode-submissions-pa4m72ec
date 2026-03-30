class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}

        for i in range(len(nums)):
            c = target - nums[i]
            if c in hashMap:
                return [hashMap[c], i]
            
            hashMap[nums[i]] = i
        