class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        res=[0]*len(nums)
        ind=0
        pi=0
        ni=1
        while(ind<len(nums)):
            if(nums[ind]<0):
                res[ni]=nums[ind]
                ni+=2
            else:
                res[pi]=nums[ind]
                pi+=2
            ind+=1
        return res