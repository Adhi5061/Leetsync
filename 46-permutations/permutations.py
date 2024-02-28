class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res=[]
        def permute(temp,curr):
            if(not temp):
                res.append(curr[:])
                return
            for i in range(0,len(temp)):
                curr.append(temp[i])
                b=temp[:i]
                b.extend(temp[i+1:])
                permute(b,curr)
                curr.pop()
        permute(nums,[])
        return(res)