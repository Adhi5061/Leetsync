class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        a=version1.split(".")
        b=version2.split(".")
        i=0
        j=0
        while(i<len(a) and j<len(b)):
            if(int(a[i])==int(b[j])):
                i+=1
                j+=1
                continue
            if(int(a[i])>int(b[j])):
                return 1
            if(int(b[j])>int(a[i])):
                return -1
        while(i!=len(a)):
            if(int(a[i])!=0):
                return 1
            i+=1
        while(j!=len(b)):
            if(int(b[j])!=0):
                return -1
            j+=1
        return 0