class Solution:
    def rob(self, nums: List[int]) -> int:
        l=len(nums)
        prev2=nums[0]
        if(l<2):
            return prev2
        prev1=max(nums[0],nums[1])
        for i in range(2,l):
            curr=max(prev1,nums[i]+prev2)
            prev2=prev1
            prev1=curr
            
        return prev1
        
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