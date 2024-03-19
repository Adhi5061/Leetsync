class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        l=0
        r=0
        curr=0
        res=float("inf")
        while(r<len(nums)):
            curr+=nums[r]
            while(curr>=target):
                res=min(res,r-l+1)
                curr-=nums[l]
                l+=1
            r+=1
        return res if res!=float("inf") else 0



        # csum=0
        # prefix=[]
        # for i in nums:
        #     if(i>target):
        #         return 1
        #     csum+=i
        #     prefix.append(csum)
        # print(prefix)
        # minv=10000
        # left=0
        # right=0
        # csum=0
        # for i in range(0,len(prefix)):
        #     if(prefix[i]>=target):
        #         j=i-1
        #         temp=prefix[i]
        #         while(temp>=target):
        #             temp-=prefix[j]
        #             j-=1


        # res=100000
        # left=0
        # right=0
        # csum=0
        # while(right<len(nums)):
        #     print(csum,left,right,res)
        #     if(csum<target):
        #         csum+=nums[right]
        #         right+=1
        #     else:
        #         res=min(res,right-left)
        #         csum-=nums[left]
        #         left+=1
            
        # return res
            