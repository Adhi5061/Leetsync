class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l=0
        r=0
        res=0
        csum=0
        d={}
        while(r<len(s)):
            if(s[r] in d):
                d[s[r]]+=1
            else:
                d[s[r]]=1
            csum+=1
            if(csum-max(d.values())>k):
                d[s[l]]-=1
                csum-=1
                l+=1
            if(csum-max(d.values())<=k):
                res=max(res,r-l+1)
            r+=1
        return res