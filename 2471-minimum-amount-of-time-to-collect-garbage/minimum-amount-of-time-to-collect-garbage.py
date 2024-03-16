class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        
        met=glass=paper=0
        ttime=0
        i=0
        gt=mt=pt=0
        while(i<len(garbage)):
            garb=garbage[i]
            met=garb.count("M")
            glass=garb.count("G")
            paper=garb.count("P")
            print(garb,met,glass,paper,ttime)
            if(i>0):
                gt+=travel[i-1]
                mt+=travel[i-1]
                pt+=travel[i-1]
            if(met):
                ttime+=met
                met=0
                ttime+=mt
                mt=0
            if(glass):
                ttime+=glass
                glass=0
                ttime+=gt
                gt=0
            if(paper):
                ttime+=paper
                paper=0
                ttime+=pt
                pt=0
            i+=1
        return ttime