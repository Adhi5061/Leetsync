class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:


        def count(k):
            l=0
            r=0
            c=0
            res=0
            while(r<len(nums)):
                if(nums[r]%2==1):
                    c+=1
                while(c>k):
                    if(nums[l]%2==1):
                        c-=1
                    l+=1
                if(c<=k):
                    res+=r-l+1
                r+=1
            return res

        return count(k)-count(k-1)