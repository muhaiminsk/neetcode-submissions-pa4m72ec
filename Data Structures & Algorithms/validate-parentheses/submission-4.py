

class Solution:
    def isValid(self, s: str) -> bool:     
        stack = []
        closeToMap = {")":"(", "}":"{","]":"["}

        for i in s:
            if i in closeToMap: 
                if stack and stack[-1] == closeToMap[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        
        return True if not stack else False
