class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        tc=0
        fc=0
        left=0
        right=0
        res=0
        while(right<len(answerKey)):
            if(answerKey[right]=="T"):
                tc+=1
            else:
                fc+=1
            while(min(tc,fc)>k):
                if(answerKey[left]=="T"):
                    tc-=1
                else:
                    fc-=1
                left+=1
            res=max(res,right-left+1)
            right+=1
        return res