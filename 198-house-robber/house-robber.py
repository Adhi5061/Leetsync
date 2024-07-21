class Solution:
    def rob(self, nums: List[int]) -> int:
        
        memo={0:nums[0]}
        def dp(n):
            if(n<0):
                return 0
            if(n in memo):
                return memo[n]
            ans= max(nums[n]+dp(n-2),dp(n-1))
            memo[n]=ans
            return ans
        return dp(len(nums)-1)