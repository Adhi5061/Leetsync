class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        c=0
        l=len(s)
        st=0
        e=l-1
        s=list(s)
        while(st<e):
            if(s[st]!=s[e]):
                if(s[st]<s[e]):
                    s[e]=s[st]
                else:
                    s[st]=s[e]
            st+=1
            e-=1
        return "".join(s)