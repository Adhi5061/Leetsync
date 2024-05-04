from collections import Counter
class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        ad=dict(Counter(nums1))
        bd=dict(Counter(nums2))
        s1=sum(nums1)
        s2=sum(nums2)
        a=ad.get(0,0)
        b=bd.get(0,0)
        if(0 not in ad or 0 not in bd):
            if(0 not in ad and 0 not in bd and s1==s2):
                return s1
            if(0 in ad and s2>=s1+a):
                return s2
            if(0 in bd and s1>=s2+b):
                return s1
            return -1
        
        # if(s1>=s2):
        #     diff=s1-s2
        #     ans=s1+max(max(diff,b),a)
        # else:
        #     diff=s2-s1
        #     ans=s2+max(max(diff,a),b)
        return max(s2+b,s1+a)