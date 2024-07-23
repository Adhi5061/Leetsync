class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        memo={}
        def dp(i,j):
            if(i<0 or j<0 or j>=len(matrix[0])):
                return 10**9
            # print(i,j)
            if((i,j) in memo):
                return memo[(i,j)]
            minv=10**9
            minv=min(minv,dp(i-1,j),dp(i-1,j-1),dp(i-1,j+1))
            if(minv==10**9):
                minv=0
            # print(minv,end=" ")
            minv+=matrix[i][j]
            memo[(i,j)]=minv
            # print(i,j,minv)
            return minv
        res=10**9
        for i in range(0,len(matrix[0])):
            res=min(res,dp(len(matrix)-1,i))
        return res