class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        nu=str(num)
        l=0
        r=k-1
        sub=nu[l:r]
        c=0
        while(r<len(nu)):
            sub+=nu[r]
            number=int(sub)
            if(number!=0 and num%number==0):
                c+=1
            sub=sub[1:]
            r+=1
        return c