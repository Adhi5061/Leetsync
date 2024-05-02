class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        memo={}

        def dp(i,j):
            if((i,j) in memo):
                return memo[(i,j)]
            if(i==len(grid)-1 and j==len(grid[0])-1):
                memo[(i,j)]=grid[i][j]
                return grid[i][j]
            if(i>=len(grid) or j>=len(grid[0])):
                memo[(i,j)]=10**5
                return 10**5
            memo[(i,j)]=grid[i][j]+min(dp(i+1,j),dp(i,j+1))
            return memo[(i,j)]
        return dp(0,0)