class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        temp=list(nums)
        for i in nums:
            if(temp[i-1]==-1):
                return i
            else:
                temp[i-1]=-1
        