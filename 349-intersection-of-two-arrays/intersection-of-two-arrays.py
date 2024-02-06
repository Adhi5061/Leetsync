class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        def present(arr,ele):
            l=0
            r=len(arr)-1
            while(l<=r):
                mid=(l+r)//2
                if(arr[mid]==ele):
                    return True
                elif(arr[mid]>ele):
                    r=mid-1
                else:
                    l=mid+1
            return False
        res=[]
        for i in nums1:
            if(i not in res and present(nums2,i)):
                res.append(i)
        return res