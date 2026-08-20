class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        res = []

        for c in nums:
            count[c] = 1 + count.get(c, 0)

        freq = [[] for i in range(len(nums)+1)]

        for n, i in count.items():
            freq[i].append(n)


        for i in range(len(freq)-1,-1,-1):
            for m in freq[i]:
                res.append(m)
                if len(res) == k:
                    return res

        
        