class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:

        table=[[float("inf")]*len(grid[0]) for _ in range(len(grid))]
        # print(table)
        table[0][0]=grid[0][0]
        for i in range(0,len(grid)):
            for j in range(0,len(grid[0])):
                if(j<len(grid[0])-1):
                    table[i][j+1]=min(table[i][j+1],table[i][j]+grid[i][j+1])
                if(i<len(grid)-1):
                    table[i+1][j]=min(table[i+1][j],table[i][j]+grid[i+1][j])
        # print(table)
        return table[-1][-1]

        # memo={}

        # def dp(i,j):
        #     if((i,j) in memo):
        #         return memo[(i,j)]
        #     if(i==len(grid)-1 and j==len(grid[0])-1):
        #         memo[(i,j)]=grid[i][j]
        #         return grid[i][j]
        #     if(i>=len(grid) or j>=len(grid[0])):
        #         memo[(i,j)]=10**5
        #         return 10**5
        #     memo[(i,j)]=grid[i][j]+min(dp(i+1,j),dp(i,j+1))
        #     return memo[(i,j)]
        # return dp(0,0)