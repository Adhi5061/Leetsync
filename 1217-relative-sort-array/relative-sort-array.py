from collections import Counter
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        d=dict(Counter(arr1))
        res=[]
        for i in arr2:
            res.extend([i]*d[i])
            del d[i]
        d=dict(sorted(d.items()))
        for i in d:
            res.extend([i]*d[i])
        # print(d)
        return res
