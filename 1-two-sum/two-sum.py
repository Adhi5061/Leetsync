class Solution(object):
    def twoSum(self, nums, target):
        d={}
        for ind,val in enumerate(nums):
            if(target-val in d):
                return [d[target-val],ind]
            d[val]=ind