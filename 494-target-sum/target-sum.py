class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo={}
        def tsum(target,pos):
            if((pos,target) in memo):
                return memo[(pos,target)]
            if(pos==len(nums)):
                if(target==0):
                    memo[(pos,target)]=1
                    return 1
                else:
                    memo[(pos,target)]=0
                    return 0
            c=0
            c+=tsum(target+nums[pos],pos+1)
            c+=tsum(target-nums[pos],pos+1)
            memo[(pos,target)]=c
            return c
        return tsum(target,0)
        