class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        d={}
        res=0
        for ind,val in enumerate(word):
            if(val in d):
                if(val.islower()):
                    d[val]=ind
            else:
                d[val]=ind
        d=dict(sorted(d.items()))
        print(d)
        for val in d:
            if(val.islower()):
                break
            if(val.lower() in d and d[val.lower()]<d[val]):
                res+=1
        return res
