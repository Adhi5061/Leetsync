class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        o={}
        for i in s:
            if i in o:
                o[i]+=1
            else:
                o[i]=1
        d={}
        for i in t:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        return(o==d)
        