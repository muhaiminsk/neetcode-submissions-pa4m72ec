class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        r = max(piles)
        l=1
        res = r

        while l<=r:
            m = (l+r)//2
            totalT = 0
            for p in piles:
                totalT += math.ceil(float(p)/m)

            if totalT<= h:
                res = m
                r= m-1

            else:
                l=m+1
        return res




            


        