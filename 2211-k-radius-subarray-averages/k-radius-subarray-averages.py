class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        if(len(nums)<=2*k):
            return([-1]*len(nums))
        res=[-1]*k
        iniv=sum(nums[0:2*k])
        d=2*k+1
        for i in range(k,len(nums)-k):
            iniv+=nums[i+k]
            res.append(iniv//d)
            iniv-=nums[i-k]
        res.extend([-1]*k)
        return res