class Solution:
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        curr=0
        for i in range(0,len(nums)):
            for j in range(i,len(nums)):
                if(abs(nums[i]-nums[j])<=min(nums[i],nums[j]) and nums[i]^nums[j]>curr):
                    curr=nums[i]^nums[j]
        return curr