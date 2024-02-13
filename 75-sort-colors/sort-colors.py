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
        z=o=t=0
        while(t<len(nums)):
            if(nums[t]==0):
                nums[t],nums[z]=nums[z],nums[t]
                z+=1
                o=max(o,z)
            elif(nums[t]==1):
                nums[t],nums[o]=nums[o],nums[t]
                o+=1
            t+=1
        temp=o
        while(temp<len(nums)):
            if(nums[temp]==1):
                nums[temp],nums[o]=nums[o],nums[temp]
                o+=1
            temp+=1