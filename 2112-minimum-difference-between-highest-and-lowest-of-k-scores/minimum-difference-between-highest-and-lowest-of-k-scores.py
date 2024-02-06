class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        left=0
        right=k-1
        minv=nums[-1]-nums[0]
        while(right<len(nums)):
            if(nums[right]-nums[left]<minv):
                minv=nums[right]-nums[left]
            right+=1
            left+=1
        return minv