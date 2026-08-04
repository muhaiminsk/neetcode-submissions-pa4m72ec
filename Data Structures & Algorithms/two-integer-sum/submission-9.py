class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}

        for i,n in enumerate(nums):
            left = target - n
            if left in hashMap:
                return [hashMap[left], i]
            hashMap[n] = i
        return []
        

        