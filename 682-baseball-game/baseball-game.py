class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack=[]
        for i in range(len(operations)):
            if((operations[i][0]>="0" and operations[i][0]<="9") or operations[i][0]=="-"):
                stack.append(int(operations[i]))
            elif(operations[i]=="C"):
                stack.pop()
            elif(operations[i]=="+"):
                stack.append(stack[-1]+stack[-2])
            else:
                stack.append(stack[-1]*2)
        print(stack)
        return sum(stack)