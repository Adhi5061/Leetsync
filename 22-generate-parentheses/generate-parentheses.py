class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res=[]
        def allpos(curr,bal,c):
            if(c==2*n):
                if(bal==0):
                    res.append(curr[:])
                return
            if(bal<n):
                allpos(curr+"(",bal+1,c+1)
            if(bal>0):
                allpos(curr+")",bal-1,c+1)
        allpos("",0,0)
        return res