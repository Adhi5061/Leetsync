class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left=0
        right=len(nums)-1
        while(left<right):
            mid=(left+right)//2
            print(left,right,nums[mid])
            if(nums[mid]>=target):
                right=mid-1
            else:
                left=mid+1
        if(nums[left]>=target):
            return left
        else:
            return left+1