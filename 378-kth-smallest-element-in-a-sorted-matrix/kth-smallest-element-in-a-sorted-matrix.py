class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        res=[]
        for i in range(0,len(matrix)):
            for j in range(0,len(matrix[0])):
                heapq.heappush(res,-matrix[i][j])
                if(len(res)>k):
                    heapq.heappop(res)
        return -heapq.heappop(res)
        