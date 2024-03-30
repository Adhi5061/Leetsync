class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        l=0
        r=0
        res=0
        d={}
        while(r<len(s)):
            if(s[r] in d):
                d[s[r]]+=1
            else:
                d[s[r]]=1
            while(len(d)==3):
                res+=len(s)-r
                d[s[l]]-=1
                if(d[s[l]]==0):
                    del d[s[l]]
                l+=1
            r+=1
        return res