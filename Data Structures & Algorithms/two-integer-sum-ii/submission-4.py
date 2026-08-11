class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        numSet = {}

        for i, n in enumerate(numbers):
            diff = target - n
            if diff in numSet:
                return [numSet[diff]+1, i+1]
            numSet[n] = i