class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        # temp=nums
        # pos=len(nums)-1
        # while(pos>=0):
        #     ele=nums[pos]
        #     ind=len(nums)-1
        #     while(ind>pos):
        #         if(nums[ind]>nums[pos]):
        #             nums[pos],nums[ind]=nums[ind],nums[pos]
        #             nums[pos+1:]=sorted(nums[pos+1:])
        #             return 
        #         ind-=1
        #     pos-=1
        # return nums.sort()
        ind=len(nums)-2
        while(ind>-1):
            if(nums[ind]<nums[ind+1]):
                break
            ind-=1
        if(ind==-1):
            nums.reverse()
            return
        ele=nums[ind]
        cmax=max(nums)
        for temp in range(ind+1,len(nums)):
            if(nums[temp]>ele and nums[temp]<=cmax):
                ci=temp
                cmax=nums[temp]
        nums[ci],nums[ind]=nums[ind],nums[ci]
        nums[ind+1:]=nums[ind+1:][::-1]