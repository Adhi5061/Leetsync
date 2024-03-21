class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # count=0
        # for i in range(0,len(nums)):
        #     csum=0
        #     for j in range(i,len(nums)):
        #         csum+=nums[j]
        #         if(csum==k):
        #             count+=1
        # return count

        prefix={0:1}
        csum=0
        count=0
        for i in nums:
            csum+=i
            if(csum-k in prefix):
                count+=prefix[csum-k]
            prefix[csum]=prefix.get(csum,0)+1
            
        return count
        