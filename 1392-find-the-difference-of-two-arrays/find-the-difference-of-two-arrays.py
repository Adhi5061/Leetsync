class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        res=[0,0]
        res[0]=list(set(nums1)-set(nums2))
        res[1]=list(set(nums2)-set(nums1))
        return res
        