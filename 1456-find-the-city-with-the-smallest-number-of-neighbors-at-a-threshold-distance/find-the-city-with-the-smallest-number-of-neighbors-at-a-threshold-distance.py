class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        matrix=[[float("inf")]*n for _ in range(n)]
        for start,end,weight in edges:
            matrix[start][end]=weight
            matrix[end][start]=weight
        for i in range(n):
            matrix[i][i]=0
        for via in range(n):
            for i in range(n):
                for j in range(n):
                    matrix[i][j]=min(matrix[i][j],matrix[i][via]+matrix[via][j])
        minc=float("inf")
        city=0
        for i in range(n):
            count=0
            for j in range(n):
                if(i!=j and matrix[i][j]<=distanceThreshold):
                    count+=1
            if(count<=minc):
                minc=count
                city=i
        # print(matrix)
        return city