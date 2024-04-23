class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        res=0
        temp=[]
        for i in word:
            if(i in temp):
                continue
            else:
                if(i.swapcase() in word):
                    res+=1
                    temp.append(i)
                    temp.append(i.swapcase())
        return res