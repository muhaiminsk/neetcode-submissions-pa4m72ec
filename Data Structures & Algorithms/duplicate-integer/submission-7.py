class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numSet = set()

        for c in nums:
            if c in numSet:
                return True
            numSet.add(c)
        return False
            

        