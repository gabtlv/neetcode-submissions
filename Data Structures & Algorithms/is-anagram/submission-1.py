class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # make sure both strings are the same length
        # sort both strings alphabetically
        # if they are the same sorted alphabetically, they are an anagram
        
        if len(s) != len(t):
            return False
        
        if sorted(s) != sorted(t):
            return False
        else:
            return True
