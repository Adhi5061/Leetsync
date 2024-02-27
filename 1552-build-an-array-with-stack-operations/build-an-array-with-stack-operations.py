class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        s=[]
        i=1
        ti=0
        while(i<=n and ti<len(target)):
            if(i==target[ti]):
                s.append("Push")
                ti+=1
            elif(i<=target[ti]):
                s.append("Push")
                s.append("Pop")
            else:
                break
            i+=1

        return s
            