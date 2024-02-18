class Solution:
    def reverseWords(self, s: str) -> str:
        res=""
        word=""
        i=len(s)-1
        while(i>=0):
            print(i,word)
            while(i>=0 and s[i]==" " ):
                if(word):
                    res+=word[::-1]+" "
                    word=""
                i-=1
            if(i>=0):
                word+=s[i]
            i-=1
        print(word,res)
        if(word):
            print("Mot a empty space",word+"jkl;")
        if(word):
            res+=word[::-1]
            print(res+"dfg")
            return res
        else:
            print(res)
            return res[:-1] 


        