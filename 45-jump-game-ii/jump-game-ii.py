class Solution:
    def jump(self, nums: List[int]) -> int:
        
        d={}
        def dp(pos):
            if(pos in d):
                return d[pos]
            if(pos==len(nums)-1):
                return 0
            if(pos>=len(nums)):
                return len(nums)
            # print(pos)
            ans=len(nums)
            for i in range(0,nums[pos]):
                ans=min(ans,1+dp(pos+i+1))
            d[pos]=ans
            return ans

        return dp(0)