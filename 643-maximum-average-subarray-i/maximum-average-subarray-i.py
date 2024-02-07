class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        val=maxv=sum(nums[:k])/k
        left=0
        right=k
        while(right<len(nums)):
            val-=nums[left]/k
            val+=nums[right]/k
            if(val>maxv):
                maxv=val
            left+=1
            right+=1
        return maxv