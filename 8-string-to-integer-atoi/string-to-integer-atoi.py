class Solution:
    def myAtoi(self, s: str) -> int:
        res=0
        f1=0
        flag=0
        fd=True
        for i in s:
            if(i==" "):
                if(fd):
                    continue
                else:
                    break
            if(i=="0"and f1==0):
                fd=False
                continue
            elif(i in "-+"):
                # print(fd,i)
                if(fd):
                    fd=False
                    if(i=="-"):
                        flag=1
                
                else:
                    break
            elif(ord(i)>=48 and ord(i)<=57):
                # print("HI")
                fd=False
                f1=1
                res*=10
                res+=int(i)
            else:
                break
        if(flag):
            res= -res
        # print(res,res<-2**31)
        if(res<-2**31):
            return -2**31
        else:
            return min(res,2**31-1)