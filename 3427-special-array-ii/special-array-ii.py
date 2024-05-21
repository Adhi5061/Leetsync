class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        prefix=[0]
        i=0
        curr=0
        while(i<len(nums)-1):
            if(nums[i]%2+nums[i+1]%2 !=1):
                curr+=1
            prefix.append(curr)
            i+=1
        res=[]
        for ind in queries:
            if(prefix[ind[1]]==prefix[ind[0]]):
                res.append(True)
            else:
                res.append(False)
        return res