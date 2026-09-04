class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        array = {0:1}

        prefix = 0 
        total = 0

        for i, n in enumerate(nums):
            prefix += n
            diff = prefix - k

            total += array.get(diff, 0)
            array[prefix] = 1 + array.get(prefix, 0)

        return total
            
        