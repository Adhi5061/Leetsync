class Solution:
    def scoreOfString(self, s: str) -> int:
        f=ord(s[1])
        se=ord(s[0])
        i=2
        res=0
        while(i<len(s)):
            res+=abs(f-se)
            se=f
            f=ord(s[i])
            i+=1
        res+=abs(f-se)
        return res