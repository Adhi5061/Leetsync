class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        
        def count(k):
            res=0
            l=0
            r=0
            d={}
            while(r<len(nums)):
                if(nums[r] in d):
                    d[nums[r]]+=1
                else:
                    d[nums[r]]=1
                while(len(d)>k):
                    d[nums[l]]-=1
                    if(d[nums[l]]==0):
                        del d[nums[l]]
                    l+=1
                if(len(d)<=k):
                    res+=r-l+1
                r+=1
            return res
        return count(k)-count(k-1)