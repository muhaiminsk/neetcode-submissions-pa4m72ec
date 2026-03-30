
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        res = 0
        l = 0
        for r in range(len(nums)):
            while nums[r] in numSet:
                numSet.remove(nums[l])
                l =+1
            numSet.add(nums[r])
            res = max(res, r-l+1)
        return res



class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for n in nums:
            if (n-1) not in numSet:
                length = 0
                while (n+length) in numSet:
                    length += 1
                longest = max(length, longest)
        return longest
