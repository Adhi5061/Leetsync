class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        left=0
        right=1
        res=0
        while(right<len(nums)):
            # if(left==right):
            #     right+=1
            #     continue
            count=1
            temp=nums[left]
            while(right<len(nums) and (temp&nums[right] ==0)):
                temp|=nums[right]
                count+=1
                right+=1
            
            res=max(res,count)
            left+=1
            right=left+1
        return max(res,1)