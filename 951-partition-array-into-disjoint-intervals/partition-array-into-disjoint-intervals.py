class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        lmi=0
        great=greatest=nums[0]
        for ind,val in enumerate(nums):
            if(val<great):
                lmi=ind
                great=greatest
            if(val>greatest):
                greatest=val
        return lmi+1

