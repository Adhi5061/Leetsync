class Solution:
    def totalFruit(self, nums: List[int]) -> int:
        l=0
        r=0
        res=0
        d={}
        while(r<len(nums)):
            if(nums[r] in d):
                d[nums[r]]+=1

            else:
                while(len(d)>1):
                    d[nums[l]]-=1
                    if(d[nums[l]]==0):
                        del d[nums[l]]
                        l+=1
                        break
                    l+=1
                d[nums[r]]=1
            res=max(res,r-l+1)
            print(res,d)
            r+=1
        return res