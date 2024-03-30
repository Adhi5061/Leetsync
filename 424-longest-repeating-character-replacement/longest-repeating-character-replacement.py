class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l=0
        r=0
        res=0
        csum=0
        mv=0
        d={}
        while(r<len(s)):
            if(s[r] in d):
                d[s[r]]+=1
            else:
                d[s[r]]=1
            csum+=1
            mv=max(mv,d[s[r]])
            if(csum-mv>k):
                d[s[l]]-=1
                csum-=1
                l+=1
            if(csum-mv<=k):
                res=max(res,r-l+1)
            r+=1
        return res