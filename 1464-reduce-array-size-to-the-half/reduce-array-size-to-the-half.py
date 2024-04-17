from collections import Counter
class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        count=Counter(arr).most_common()
        # count.sort(reverse=True
        len1=len(arr)
        len2=0
        res=0
        for ind,val in count:
            len2+=val
            res+=1
            if(len2>=(len1/2)):
                return res
        return res
