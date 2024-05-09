class Solution:
    def maximumHappinessSum(self, hapiness: List[int], k: int) -> int:
        hapiness.sort(reverse=True)
        res=0
        for i in range(k):
            cv=hapiness[i]-i
            if(cv<0):
                return res
            res+=cv
        return res