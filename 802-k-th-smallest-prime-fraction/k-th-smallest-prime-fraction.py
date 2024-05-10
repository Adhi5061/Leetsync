import heapq
class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        res=[]
        for i in range(0,len(arr)):
            for j in range(i,len(arr)):
                heapq.heappush(res,[arr[i]/arr[j],arr[i],arr[j]])
        for i in range(k-1):
            heapq.heappop(res)
        return heapq.heappop(res)[1:]