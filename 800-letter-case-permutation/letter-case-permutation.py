class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        res=[]
        t="0123456789"
        l=len(s)
        def per(curr,pos):
            if(pos==l):
                res.append(curr)
                return
            if(s[pos] in t):
                curr+=s[pos]
                per(curr,pos+1)
            else:
                curr+=s[pos]
                per(curr,pos+1)
                curr=curr[:-1]
                curr+=s[pos].swapcase()
                per(curr,pos+1)
        per("",0)
        return res