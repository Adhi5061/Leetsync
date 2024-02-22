class MinStack:

    def __init__(self):
        self.stack=[]
        self.mstack=[]
        self.topv=-1        

    def push(self, val: int) -> None:
        self.topv+=1
        self.stack.append(val)
        if(self.topv>0):
            if(val<self.mstack[self.topv-1]):
                self.mstack.append(val)
            else:
                self.mstack.append(self.mstack[self.topv-1])
        else:
            self.mstack.append(val)

    def pop(self) -> None:
        if(self.topv>-1):
            self.stack.pop()
            self.mstack.pop()
            self.topv=self.topv-1

    def top(self) -> int:
        if(self.topv>-1):
            return(self.stack[self.topv])
    def getMin(self) -> int:
        if(self.topv>-1):
            return self.mstack[self.topv]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()