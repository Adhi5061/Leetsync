class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        
        memo={}
        def dp(i,j):
            if((i,j) in memo):
                return memo[(i,j)]
            if(i==len(triangle) or j>=len(triangle[i])):
                return 0
            ans=triangle[i][j]+min(dp(i+1,j),dp(i+1,j+1))
            memo[(i,j)]=ans
            return ans  

        return dp(0,0)