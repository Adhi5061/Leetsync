class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        if(k==0):
            return([0]*len(code))
        l=1
        le=len(code)
        if(k<0):
            l=len(code)+k
        r=(l+abs(k)-1)%le
        csum=sum(code[l:r+1])
        res=[]
        for i in code:
            print(l,r,csum)
            res.append(csum)
            csum-=code[l]
            l=(l+1)%le
            r=(r+1)%le
            csum+=code[r]
        return res