class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack=nums[::-1]
        res=[0]*len(nums)
        for i in range(len(nums)-1,-1,-1):
            while(len(stack)>0 and stack[-1]<=nums[i]):
                stack.pop()
            if(stack):
                res[i]=stack[-1]
            else:
                res[i]=-1
            stack.append(nums[i])
        return res