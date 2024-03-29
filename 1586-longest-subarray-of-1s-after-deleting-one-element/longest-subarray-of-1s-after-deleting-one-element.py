class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        
        l=0
        r=0
        t=0
        res=0
        while(r<len(nums)):
            if(nums[r]==0 ):
                if(t==1):
                    res=max(res,r-l-1)
                    l=pos+1
                    pos=r
                else:
                    t=1
                    pos=r
            r+=1
        res=max(res,r-l-1)
        return res