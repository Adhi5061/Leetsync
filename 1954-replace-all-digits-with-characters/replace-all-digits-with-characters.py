class Solution:
    def replaceDigits(self, s: str) -> str:
        res=""
        for i in range(0,len(s)):
            if(i%2==0):
                res+=s[i]
            else:
                res+=chr(ord(s[i-1])+int(s[i]))
        return res
        