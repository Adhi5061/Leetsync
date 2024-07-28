class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        stack=[]
        pse=[]
        for i in range(0,len(nums)):
            while(stack and nums[stack[-1]]>nums[i]):
                stack.pop()
            pse.append(stack[-1] if stack else -1)
            stack.append(i)
        stack=[]
        nse=[]
        for i in range(len(nums)-1,-1,-1):
            # print(i)
            while(stack and nums[stack[-1]]>=nums[i]):
                stack.pop()
            nse.append(stack[-1] if stack else len(nums))
            stack.append(i)
        nse=nse[::-1]
        
        minv=0
        for i in range(0,len(nums)):
            left=i-pse[i]
            right=nse[i]-i
            c=left*right*nums[i]
            minv=(minv+c)
        



        stack=[]
        pge=[]
        for i in range(0,len(nums)):
            while(stack and nums[stack[-1]]<nums[i]):
                stack.pop()
            pge.append(stack[-1] if stack else -1)
            stack.append(i)
        stack=[]
        nge=[]
        for i in range(len(nums)-1,-1,-1):
            # print(i)
            while(stack and nums[stack[-1]]<=nums[i]):
                stack.pop()
            nge.append(stack[-1] if stack else len(nums))
            stack.append(i)
        nge=nge[::-1]

        maxv=0
        for i in range(0,len(nums)):
            left=i-pge[i]
            right=nge[i]-i
            c=left*right*nums[i]
            maxv+=c
        # print(pge,"\n",nge)
        return maxv-minv