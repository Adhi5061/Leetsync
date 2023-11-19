class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        l=len(s)
        v=0
        for i in range(0,l//2):
            if(s[i] in "aeiou AEIOU"):
                v+=1
        for i in range(l//2,l):
            if(s[i] in "aeiou AEIOU"):
                v-=1
        return(v==0)
        