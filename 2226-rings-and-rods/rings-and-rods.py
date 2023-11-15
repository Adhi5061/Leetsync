class Solution:
    def countPoints(self, rings: str) -> int:
        d={}
        for i in range(10):
            d[str(i)]=""
        for i in range(0,len(rings),2):
            if(rings[i] in d[rings[i+1]]):
                continue
            else:
                d[rings[i+1]]+=rings[i]
        c=0
        for i in d:
            if("B" in d[i] and "G" in d[i] and "R" in d[i]):
                c+=1
        return c
        