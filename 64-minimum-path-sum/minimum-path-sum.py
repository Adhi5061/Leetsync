class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        memo={(0,0):grid[0][0]}
        def dp(i,j):
            if((i,j) in memo):
                return memo[(i,j)]
            if(i<0 or j<0):
                return 1000000
            ans=grid[i][j]+min(dp(i-1,j),dp(i,j-1))
            memo[(i,j)]=ans
            # print(i,j,ans)
            return ans
        return dp(len(grid)-1,len(grid[0])-1)