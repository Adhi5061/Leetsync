class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        
        res=[]
        def sub(curr,pos):
            if(pos==len(nums)):
                if(len(curr)==0):
                    return 0
                # print(curr)
                res.append(curr[:])
                return 1
            a=sub(curr,pos+1)
            for i in curr:
                if(abs(nums[pos]-i)==k):
                    return a
            curr.append(nums[pos])
            b=sub(curr,pos+1)
            curr.pop()
            return a+b
        ans=sub([],0)
        # print(res)
        return ans