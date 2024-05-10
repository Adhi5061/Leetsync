class Solution:
    def rob(self, nums: List[int]) -> int:
        memo={}
        def dp(i,f):
            if((i,f) in memo):
                return memo[(i,f)]
            if(i==0):
                return max(nums[i]+dp(i+2,1),dp(i+1,0))
            if(i>=len(nums)):
                return 0
            if(i==len(nums)-1):
                if(f):
                    return 0
                else:
                    return nums[i]
            a=nums[i]+dp(i+2,f)
            b=dp(i+1,f)
            memo[(i,f)]=max(a,b)
            return max(a,b)
        return dp(0,0)