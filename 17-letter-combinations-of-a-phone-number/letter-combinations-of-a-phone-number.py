class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        d={"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
        res=[]
        l=len(digits)
        def lc(pos,curr):
            if(pos==l):
                if(l==0):
                    return res
                res.append(curr)
                return 
            st=d[digits[pos]]
            for i in st:
                curr+=i
                lc(pos+1,curr)
                curr=curr[:-1]
        lc(0,"")
        return res

