class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums=sorted(nums)
        mid=len(nums)//2
        i=mid-1
        j=mid
        maxv=nums[i]+nums[j]
        while(i>=0):
            sumv=nums[i]+nums[j]
            i-=1
            j+=1
            if(sumv>maxv):
                maxv=sumv
        return(maxv)
        