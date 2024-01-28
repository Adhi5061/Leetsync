class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l=len(prices)
        profit=0
        minp=prices[0]
        for i in prices:
            if(i<minp):
                minp=i
            elif(i-minp>profit):
                profit=i-minp
        return(profit)