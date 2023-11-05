class Solution:
    def sortSentence(self, s: str) -> str:
        temp=s.split()
        maxv=0
        for i in temp:
            if(int(i[-1])>maxv):
                maxv=int(i[-1])
        res=[0]*maxv
        for i in temp:
            res[int(i[-1])-1]=i[:-1]
        return(" ".join(res))