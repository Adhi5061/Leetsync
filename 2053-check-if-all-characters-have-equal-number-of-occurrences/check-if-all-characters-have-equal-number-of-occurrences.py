class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        d={}
        for i in s:
            if(i in d):
                d[i]+=1
            else:
                d[i]=1
        arr=list(d.values())
        v=arr[0]
        for i in arr:
            if(i!=v):
                return False
        return True