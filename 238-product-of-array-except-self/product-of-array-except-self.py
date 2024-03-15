class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix=[]
        curr=1
        for i in nums:
            prefix.append(curr)
            curr=curr*i
        curr=1
        suffix=[1]*len(nums)
        for i in range(len(nums)-1,-1,-1):
            suffix[i]=curr
            curr*=nums[i]
        res=[]
        for i in range(0,len(nums)):
            res.append(prefix[i]*suffix[i])
        return res
        
        
        # count=0
        # res=1
        # l=len(nums)
        # for i in nums:
        #     if(i==0):
        #         count+=1
        #         continue
        #     else:
        #         res=res*i
        # if count>1:
        #     return([0]*l)
        # elif count==1:
        #     for i in range(0,l):
        #         if(nums[i]!=0):
        #             nums[i]=0
        #         else:
        #             nums[i]=res
        #     return(nums)
        
        # for i in range(0,l):
        #     nums[i]=int(res/nums[i])
        # return(nums)
