class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        res=csum=0
        left=right=0
        window=set()
        while(right<len(nums)):
            if(nums[right] in window):
                res=max(res,csum)
                while(nums[right] in window):
                    csum-=nums[left]
                    window.remove(nums[left])
                    left+=1
            else:
                window.add(nums[right])
                csum+=nums[right]
                right+=1
                
        return max(res,csum)