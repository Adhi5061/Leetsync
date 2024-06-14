class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        curr=nums[0]-1
        res=0
        # print(nums)
        for num in nums:
            
            if(num<=curr):
                res+=curr-num+1
                curr+=1
            else:
                curr=num
            # print(curr,num,res)
        return res
