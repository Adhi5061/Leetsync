class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        if(k==len(cardPoints)):
            return sum(cardPoints)
        csum=sum(cardPoints[:k])
        l=0
        r=k
        res=csum
        while(r!=0):
            r-=1
            l-=1
            csum-=cardPoints[r]
            csum+=cardPoints[l]
            res=max(res,csum)
        return res