class Solution:
    def convert(self, s: str, numRows: int) -> str:
        d=[[] for _ in range(numRows)]
        r=0
        c=0
        ind=0
        if(numRows==1):
            return s
        while(True):
            if(ind>=len(s)):
                break
            while(r<numRows):
                if(ind>=len(s)):
                    break
                i=s[ind]
                ind+=1
                d[r].append(i)
                r+=1
            r=numRows-2
            while(r>=0):
                if(ind>=len(s)):
                    break
                i=s[ind]
                ind+=1
                d[r].append(i)
                r-=1
            r=1
        res=""
        for i in d:
            res+="".join(i)
        return res