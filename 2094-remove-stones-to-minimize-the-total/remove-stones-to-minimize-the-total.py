import math
import heapq
class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        heap=[-i for i in piles]
        heapq.heapify(heap)
        for i in range(k):
            heapq.heapreplace(heap,heap[0]//2)
            # t=-heapq.heappop(heap)
            # newv=math.ceil(t/2)
            # # print(t,newv)
            # heapq.heappush(heap,-newv)
        return -sum(heap)