class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        count = 0
        for ch in t:
            if count < len(s) and s[count] == ch:
                count+=1
        
        return count == len(s)

                   