class Solution:
    def countAsterisks(self, s: str) -> int:
        c=0
        res=0
        for i in s:
            if(i=="*" and c==0):
                res+=1
            elif(i=="|"):
                c=(c+1)%2
        return res

                
        