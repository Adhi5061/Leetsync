class Solution:
    def countVowelStrings(self, n: int) -> int:
        arr=["a","e","i","o","u"]
        memo={}
        def vowel(pos,noe):
            if((pos,noe) in memo):
                
                return memo[(pos,noe)]
            if(noe==n):
                return 1
            if(pos==5):
                return 0
            c=0
            for i in range(pos,5):
                t=vowel(i,noe+1)
                if(t):
                    c+=t
            memo[(pos,noe)]=c
            return c
        return vowel(0,0)
                