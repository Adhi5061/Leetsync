class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        dp=[[0]*len(nums) for i in range(len(nums))]
        dp[0][0]=1
        for i in range(1,len(nums)):
            ele=nums[i]
            maxv=0
            for j in range(0,i):
                dp[i][j]=dp[i-1][j]
                if(nums[j]<ele):
                    maxv=max(maxv,dp[i-1][j])
            dp[i][i]=1+maxv
        return max(dp[-1])
        # memo={}
        # def dp(i,last):
        #     if(i==len(nums)):
        #         return 0
        #     if((i,last) in memo):
        #         return memo[(i,last)]
        #     a=0
        #     if(nums[i]>last):
        #         a=1+dp(i+1,nums[i])
        #     b=dp(i+1,last)
        #     memo[(i,last)]=max(a,b)
        #     return max(a,b)
        # return dp(0,-10**5)