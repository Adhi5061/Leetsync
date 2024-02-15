class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left=0
        right=len(nums)-1
        ans=len(nums)
        while(left<=right):
            mid=(left+right)//2
            if(nums[mid]>=target):
                ans=mid
                right=mid-1
            else:
                left=mid+1
        # if(nums[left]>=target):
        #     return left
        # else:
        #     return left+1
        return ans