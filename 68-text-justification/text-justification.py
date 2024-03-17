class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        i=0
        currlen=0
        start=0
        fin=[]
        while(i<len(words)):
            string=words[i]
            if(currlen+len(string)>maxWidth):
                currlen-=1
                extra=maxWidth-currlen
                noword=i-start-1
                res=""
                if(noword==0):
                    res+=words[i-1]
                    res+=" "*(maxWidth-currlen)
                else:
                    space=extra//noword+1
                    e=extra%noword
                    
                    for j in range(start,i-1):
                        res+=words[j]
                        if(e>0):
                            res+=" "*(space+1)
                            e-=1
                        else:
                            res+=" "*space
                    res+=words[i-1]
                fin.append(res)
                start=i
                currlen=0
            else:
                currlen+=len(string)+1
                i+=1
        res=""
        for j in range(start,i-1):
            res+=words[j]
            res+=" "
        res+=words[i-1]
        res+=" "*(maxWidth-len(res))
        fin.append(res)
        return fin