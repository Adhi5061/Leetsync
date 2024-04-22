import math
import heapq
class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        res=sum(piles)
        heap=[-i for i in piles]
        heapq.heapify(heap)
        for i in range(k):
            t=-heapq.heappop(heap)
            newv=math.ceil(t/2)
            # print(t,newv)
            res-=newv
            heapq.heappush(heap,-newv)
        return -sum(heap)