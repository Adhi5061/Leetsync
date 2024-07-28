class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack=[]
        res=[]
        l=len(nums)
        for i in range(2*l-1,-1,-1):
            while(stack and stack[-1]<=nums[i%l]):
                stack.pop()
            
            if(stack and i<l):
                res.insert(0,stack[-1])
            elif(i<l):
                res.insert(0,-1)
            stack.append(nums[i%l])
        return res