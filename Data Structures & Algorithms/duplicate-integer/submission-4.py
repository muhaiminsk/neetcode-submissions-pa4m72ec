class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashSet = set()

        for c in nums:
            if c in hashSet:
                return True
            else:
                hashSet.add(c)
        return False