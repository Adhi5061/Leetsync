class Solution:
    def interpret(self, command: str) -> str:
        res=""
        v=0
        for i in command:
            if(i in "Gal"):
                res+=i
                v=0
            elif(i=="("):
                v+=1
            elif(i==")" and v==1):
                res+="o"
                v=0
        return res
        