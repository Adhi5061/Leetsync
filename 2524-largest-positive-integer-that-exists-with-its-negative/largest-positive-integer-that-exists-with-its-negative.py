class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        nums.sort()
        l=0
        r=len(nums)-1
        while(l<r):
            if(nums[l]+nums[r]==0):
                return nums[r]
            elif(nums[l]+nums[r]>0):
                r-=1
            else:
                l+=1
        return -1