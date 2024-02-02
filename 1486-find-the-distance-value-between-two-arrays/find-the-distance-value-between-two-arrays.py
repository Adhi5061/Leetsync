class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        c=0
        arr2.sort()
        for num in arr1:
            l=0
            r=len(arr2)-1
            close=10000
            while(l<=r):
                mid=(l+r)//2
                if(abs(num-arr2[mid])<close):
                    close=abs(num-arr2[mid])
                if(close==0):
                    break
                if(arr2[mid]>num):
                    r=mid-1
                else:
                    l=mid+1
            if(close>d):
                c+=1
        return c