class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        i=0
        res=0
        piles.sort(reverse=True)
        while(i<2*len(piles)/3):
            res+=piles[i+1]
            i+=2
        return res