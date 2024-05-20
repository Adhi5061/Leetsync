class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        i=0
        while(i<len(nums)-1):
            if((nums[i]%2)+(nums[i+1]%2)!=1):
                return False
            i+=1
        return True