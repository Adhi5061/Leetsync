class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        memo={}
        def sub(target,i):
            if((target,i) in memo):
                return memo[(target,i)]
            if(target==0):
                memo[(target,i)]=True
                return True
            if(i==len(nums)):
                memo[(target,i)]=False
                return False
            if(sub(target,i+1)):
                memo[(target,i)]=True
                return True
            if(sub(target-nums[i],i+1)):
                memo[(target,i)]=True
                return True
            memo[(target,i)]=False
            return False
        if(sum(nums)%2!=0):
            return False
        return sub(sum(nums)/2,0)