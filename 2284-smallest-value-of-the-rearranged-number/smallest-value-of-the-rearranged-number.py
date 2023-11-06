class Solution:
    def smallestNumber(self, num: int) -> int:
        def compare1(a,b):
            if(a+b<b+a):
                return -1
            else:
                return(1)
        if(num>0):
            lis=[i for i in str(num)]
        else:
            lis=[i for i in str(num)[1:]]
        
        lis=sorted(lis,key=cmp_to_key(compare1))
        res=""
        c=0
        if(num<0):
            lis.reverse()
            return(-int("".join(lis)))
        for i,n in enumerate(lis):
            if(n=='0'):
                c+=1
            else:
                res+=n
                res+="0"*c
                c=0
        res+="0"*c

        return(int(res) if res else 0)
                