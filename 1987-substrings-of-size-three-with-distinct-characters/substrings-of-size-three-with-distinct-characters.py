class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        c=0
        for i in range(0,len(s)-2):
            if(len(set(s[i:i+3]))==3):
                c+=1
        return c