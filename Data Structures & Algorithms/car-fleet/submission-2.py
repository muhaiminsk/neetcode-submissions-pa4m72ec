class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack=[]
        pairs = []
        for i in range(len(speed)):
            pairs.append((position[i],speed[i]))

        pairs.sort()

        for p, s in pairs[::-1]:
            stack.append((target - p)/s)
            if len(stack) >=2 and stack[-1]<= stack[-2]:
                stack.pop()
        return len(stack)



        
            



        