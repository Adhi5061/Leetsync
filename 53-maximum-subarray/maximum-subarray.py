class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        si=-1
        i=0
        cs=0
        ms=-100000000
        while(i<len(nums)):
            cs+=nums[i]
            if(cs>ms):
                ms=cs
                res=i-si
            if(cs<=0):
                si=i
                cs=0
            i+=1
        return ms