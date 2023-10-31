class Solution(object):
    def twoSum(self, nums, target):
        l=len(nums)
        val=0
        for i in range(0,l,1):
            for j in range(i+1,l,1):
                if(nums[i]+nums[j]==target):
                    res=(i,j)
                    return(list(res))
                    val=1
                    break
            if(val==1):
                break