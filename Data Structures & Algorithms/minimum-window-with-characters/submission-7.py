class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        countT, window = {}, {}

        for i in range(len(t)):
            countT[t[i]] = 1 + countT.get(t[i], 0)

        res, resLen = [-1,-1], float("infinity")
        have, need = 0, len(countT)
        l=0

        for r in range(len(s)):
            c = s[r]
            window[s[r]] = 1 + window.get(s[r], 0)

            if c in countT and countT[s[r]] == window[s[r]]:
                have += 1

            while have == need:
                if (r-l+1)<resLen:
                    resLen = r-l+1
                    res = [l,r]

                window[s[l]] -= 1

                if s[l] in countT and countT[s[l]] > window[s[l]]:
                    have-=1
                l+=1
        l, r = res
        return s[l:r+1] if resLen != float("infinity") else ""


        