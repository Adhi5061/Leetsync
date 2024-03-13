class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        
        d={}
        ind=0
        build=buildings[0]
        while(1):
            #print(build)
            temp=1
            #print("Outer d",d)
            summa=0
            for j in d:
                #print(d)
                curr=j
                val=d[j]
                if(build[0] >=j[0] and build[0] < j[1]):
                    temp=0
                    if(build[2]>val):
                        #print("deleted:",j,d[j])
                        del d[j]
                        if(curr[0]<build[0]):
                            d[(curr[0],build[0])]=val
                        d[(build[0],min(curr[1],build[1]))]=build[2]
                        #print(d)
                        if(curr[1]>build[1]):
                            d[(build[1],curr[1])]=val
                        if(build[1]>curr[1]):
                            build=[j[1],build[1],build[2]]
                            #print("Summa set to 1 inside loop",build)
                            summa=1
                        
                        break
                    if(build[1]>curr[1]):
                        build=[j[1],build[1],build[2]]
                        #print("Summa set to 1",build)
                        summa=1
                        break
            if(summa):
                continue
            if(temp):
                d[(build[0],build[1])]=build[2]
            ind+=1
            if(ind>=len(buildings)):
                break
            build=buildings[ind]
        #print("Final d:",d)
        res=[]
        preval=0
        prer=buildings[0][0]
        first=0
        #print("\n\n")
        d = {k: d[k] for k in sorted(d)}
        for i in d:
            #print(i,d[i],res,preval,prer)
            foruse=i
            if(first and prer!=i[0]):
                res.append([prer,0])
                preval=0
            first=1
            if(d[i]==preval and i[0]==prer):
                prer=i[1]
                continue
            elif(d[i]<preval):
                res.append([i[0],d[i]])
            else:
                res.append([i[0],d[i]])
            preval=d[i]
            prer=i[1]
        res.append([foruse[-1],0])
        #print(res)
        return res
                