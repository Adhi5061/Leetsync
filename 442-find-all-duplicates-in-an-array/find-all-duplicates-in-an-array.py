class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res=[]
        for i in nums:
            if(nums[abs(i)-1]<0):
                res.append(abs(i))
            else:
                nums[abs(i)-1]=-nums[abs(i)-1]
        return res
        # d={}
        # for i in nums:
        #     d[i]=d.get(i,0)+1
        # res=[]
        # for i in d:
        #     if(d[i]>1):
        #         res.append(i)
        # return res