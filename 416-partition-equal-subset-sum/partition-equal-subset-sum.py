class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n=len(nums)
        t=sum(nums)
        if(t%2==1):
            return False
        t=t//2
        dp=[[False]*(t+1) for i in range(len(nums))]
        # print(t)
        for i in range(n):
            dp[i][0]=True
        if(nums[0]==t):
            return True
        if(nums[0]<=t):
            dp[0][nums[0]]=True
        for i in range(1,n):
            ele=nums[i]
            # print(i,ele,dp[i-1])
            for j in range(1,t+1):
                nottaken=dp[i-1][j]
                taken=False
                if(ele<=j):
                    taken=dp[i-1][j-ele]
                dp[i][j]=(nottaken or taken)
        # for row in dp:
        #     print(row)
        return dp[-1][-1]
        # memo={}
        # def dp(i,target):
        #     if(target==0):
        #         return True
        #     if(i==-1):
        #         if(target==0):
        #             return True
        #         return False
        #         # return False
        #     if((i,target) in memo):
        #         return memo[(i,target)]
        #     ans=dp(i-1,target-nums[i]) or dp(i-1,target)
        #     memo[(i,target)]=ans
        #     return ans
        # s=sum(nums)
        # if(s%2==1):
        #     return False
        # return dp(len(nums)-1,s//2)