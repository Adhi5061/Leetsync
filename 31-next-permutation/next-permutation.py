class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        temp=nums
        pos=len(nums)-1
        while(pos>=0):
            ele=nums[pos]
            ind=len(nums)-1
            while(ind>pos):
                if(nums[ind]>nums[pos]):
                    nums[pos],nums[ind]=nums[ind],nums[pos]
                    nums[pos+1:]=sorted(nums[pos+1:])
                    return 
                ind-=1
            pos-=1
        return nums.sort()