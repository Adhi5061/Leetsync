class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        
        memo={}
        def dp(i,j):
            if((i,j) in memo):
                return memo[(i,j)]
            if(i<0 or j<0 or i>len(matrix) or j>=len(matrix)):
                return 10**5
            if(i==len(matrix)):
                return 0
            ans=matrix[i][j]+min(dp(i+1,j),dp(i+1,j-1),dp(i+1,j+1))
            memo[(i,j)]=ans
            return ans

        ans=10**5
        for i in range(0,len(matrix)):
            ans=min(ans,dp(0,i))
        return ans