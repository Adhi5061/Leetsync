class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        memo={}
        def dp(i,target):
            if(i==-1):
                if(target==0):
                    return True
                return False
                # return False
            if((i,target) in memo):
                return memo[(i,target)]
            ans=dp(i-1,target-nums[i]) or dp(i-1,target)
            memo[(i,target)]=ans
            return ans
        s=sum(nums)
        if(s%2==1):
            return False
        return dp(len(nums)-1,s//2)