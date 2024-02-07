class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vow="aeiou"
        ccount=0
        for i in range(k):
            if(s[i] in vow):
                ccount+=1
        res=ccount
        left=0
        right=k
        while(right<len(s)):
            if(s[left] in vow):
                ccount-=1
            if(s[right] in vow):
                ccount+=1
            left+=1
            right+=1
            res=max(res,ccount)
            if(res==k):
                return res
        return res