import heapq
class Solution:
    def maximumScore(self, a: int, b: int, c: int) -> int:
        count=0
        heap=[]
        heapq.heappush(heap,-a)
        heapq.heappush(heap,-b)
        heapq.heappush(heap,-c)
        while(1):
            f=-heapq.heappop(heap)
            s=-heapq.heappop(heap)
            if(f==0 or s==0):
                break
            count+=1
            heapq.heappush(heap,-(f-1))
            heapq.heappush(heap,-(s-1))
        return count