class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False

        countM = {}

        for c in magazine:
            countM[c] = 1+ countM.get(c, 0)

        for c in ransomNote:
            if countM.get(c, 0) == 0:
                return False
            
            countM[c] -= 1
            
        return True


        