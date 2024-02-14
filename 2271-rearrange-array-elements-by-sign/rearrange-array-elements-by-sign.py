class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        res=[]
        ind=0
        pos=0
        neg=0
        while(ind<len(nums)):
            while(nums[pos]<0):
                pos+=1
            while(nums[neg]>0):
                neg+=1
            res.append(nums[pos])
            res.append(nums[neg])
            pos+=1
            neg+=1
            ind+=2
        return res