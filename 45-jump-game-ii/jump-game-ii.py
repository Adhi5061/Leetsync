class Solution:
    def jump(self, nums: List[int]) -> int:
        
        dp=[float("inf") for i in range(0,len(nums))]
        dp[0]=0
        for i in range(0,len(nums)):
            for j in range(i+1,i+nums[i]+1):
                if(j>=len(nums)):
                    break
                dp[j]=min(dp[j],dp[i]+1)
        return dp[-1]
        # d={}
        # def dp(pos):
        #     if(pos in d):
        #         # print("hi")
        #         return d[pos]
        #     if(pos>=len(nums)-1):
        #         return 0
        #     # if(pos>=len(nums)):
        #     #     return len(nums)
        #     # print(pos)
        #     ans=len(nums)
        #     for i in range(0,nums[pos]):
        #         ans=min(ans,1+dp(pos+i+1))
        #     d[pos]=ans
        #     return ans

        # return dp(0)