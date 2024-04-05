class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        l=0
        r=0
        d={}
        length=0
        while(r<len(nums)):
            if(nums[r] in d):
                d[nums[r]]+=1
            else:
                d[nums[r]]=1
            while(d[nums[r]]>k):
                d[nums[l]]-=1
                l+=1
            
            length=max(length,r-l+1)
            r+=1
        return length