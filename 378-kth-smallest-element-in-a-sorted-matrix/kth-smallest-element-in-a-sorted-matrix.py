class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        res=[]
        for i in range(0,len(matrix)):
            if(len(res)==k and -res[0]<matrix[i][0]):
                    # t=1
                    break
            for j in range(0,len(matrix[0])):
                if(len(res)==k and -res[0]<matrix[i][j]):
                    # t=1
                    break
                heapq.heappush(res,-matrix[i][j])
                if(len(res)>k):
                    heapq.heappop(res)
        return -heapq.heappop(res)
        