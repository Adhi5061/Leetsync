class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit=0
        minp=prices[0]
        l=len(prices)
        for i in prices:
            if(i<minp):
                minp=i
            else:
                profit+=(i-minp)
                minp=i
        return profit