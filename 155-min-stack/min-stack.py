class MinStack:

    def __init__(self):
        self.stack=[]
        self.minstack=[]
        self.minv=float("inf")

    def push(self, val: int) -> None:
        self.stack.append(val)
        if(val<self.minv):
            self.minv=val
        self.minstack.append(self.minv)

    def pop(self) -> None:
        self.minstack.pop()
        if(not self.minstack):
            self.minv=float("inf")
        else:
            self.minv=self.getMin()
        return self.stack.pop()
        

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minstack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()