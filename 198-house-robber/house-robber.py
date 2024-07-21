class Solution:
    def rob(self, nums: List[int]) -> int:
        l=len(nums)
        dp=[-1]*l
        dp[0]=nums[0]
        if(l<2):
            return dp[0]
        dp[1]=max(nums[0],nums[1])
        for i in range(2,l):
            dp[i]=max(dp[i-1],nums[i]+dp[i-2])
        return dp[-1]
        # memo={0:nums[0]}
        # def dp(n):
        #     if(n<0):
        #         return 0
        #     if(n in memo):
        #         return memo[n]
        #     ans= max(nums[n]+dp(n-2),dp(n-1))
        #     memo[n]=ans
        #     return ans
        # return dp(len(nums)-1)