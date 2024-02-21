class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res=[]
        l=len(nums)
        nums.sort()
        def sub(curr,pos):
            if(pos==l):
                if(curr[:] not in res):
                    res.append(curr[:])
                return
            sub(curr,pos+1)
            curr.append(nums[pos])
            sub(curr,pos+1)
            curr.pop()
        sub([],0)
        return res