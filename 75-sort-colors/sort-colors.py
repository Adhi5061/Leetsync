class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # pos=0
        # for j in range(3):
        #     for i in range(pos,len(nums)):
        #         if(nums[i]==j):
        #             nums[pos],nums[i]=nums[i],nums[pos]
        #             pos+=1
        # 
        l=m=0
        r=len(nums)-1
        while(m<=r):
            if(nums[m]==1):
                m+=1
            elif(nums[m]==0):
                nums[m],nums[l]=nums[l],nums[m]
                l+=1
                m+=1
            else:
                nums[m],nums[r]=nums[r],nums[m]
                r-=1
