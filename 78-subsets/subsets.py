class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[]
        l=len(nums)
        def sub(curr,pos):
            if(pos==l):
                res.append(curr[:])
                return
            sub(curr,pos+1)
            curr.append(nums[pos])
            sub(curr,pos+1)
            curr.pop()
        sub([],0)
        return res