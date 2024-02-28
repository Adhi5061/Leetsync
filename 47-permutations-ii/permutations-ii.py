class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res=[]
        nums.sort()
        def permute(temp,curr):
            if(not temp):
                res.append(curr[:])
                return
            for i in range(0,len(temp)):
                if(i>0 and temp[i]==temp[i-1]):
                    continue
                curr.append(temp[i])
                b=temp[:i]
                b.extend(temp[i+1:])
                permute(b,curr)
                curr.pop()
        permute(nums,[])
        return(res)