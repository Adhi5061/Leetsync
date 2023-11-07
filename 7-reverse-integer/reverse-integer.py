class Solution:
    def reverse(self, x: int) -> int:
        t=abs(x)
        res=0
        while(t>0):
            res=res*10
            res+=t%10  
            if(res>2**31):
                return 0
            t=t//10
        if(x<0):
            return(-res)
        else:
            if(res>=2**31):
                return 0
            return res