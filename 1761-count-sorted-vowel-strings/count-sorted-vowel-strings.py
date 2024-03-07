class Solution:
    def countVowelStrings(self, n: int) -> int:
        arr=["a","e","i","o","u"]
        def vowel(pos,noe):
            if(noe==n):
                return 1
            if(pos==5):
                return 0
            c=0
            for i in range(pos,5):
                t=vowel(i,noe+1)
                if(t):
                    c+=t
            return c
        return vowel(0,0)
                