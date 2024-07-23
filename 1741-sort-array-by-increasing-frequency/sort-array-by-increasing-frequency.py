class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        d={}
        for i in nums:
            d[i]=d.get(i,0)+1
        d=dict(sorted(d.items(), key=lambda x:(x[1],-x[0])))
        res=[]
        for key,value in d.items():
            res.extend([key]*value)
        return res