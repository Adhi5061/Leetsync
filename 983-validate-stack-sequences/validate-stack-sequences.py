class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack=[]
        i=0
        for char in pushed:
            stack.append(char)
            while(stack and stack[-1]==popped[i]):
                stack.pop()
                i+=1
        return len(stack)==0