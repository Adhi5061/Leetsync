import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left=1
        right=max(piles)
        while(left<=right):
            mid=(left+right)//2
            timetaken=0
            for pile in piles:
                timetaken+=math.ceil(pile/mid)
            if(timetaken>h):
                left=mid+1
            else:
                result=mid
                right=mid-1
        return result