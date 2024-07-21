class Solution:
    def rob(self, nums: List[int]) -> int:
        memo={}
        if(len(nums)==1):
            return nums[0]
        def dp(n,flag):
            if(n<0):
                return 0
            if((n,flag) in memo):
                return memo[(n,flag)]
            if(n==0):
                if(flag):
                    return 0
                else:
                    return nums[0]
            memo[(n,flag)]=max(dp(n-1,flag),nums[n]+dp(n-2,flag))
            # print(n,memo[n])
            return memo[(n,flag)]
        return max(dp(len(nums)-1,True),dp(len(nums)-2,False))