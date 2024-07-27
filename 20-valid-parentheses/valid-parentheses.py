class Solution:
    def isValid(self, s: str) -> bool:
        d={"(":")","{":"}","[":"]"}
        stack=[]
        for inp in s:
            if(inp in d):
                stack.append(d[inp])
            else:
                if(not stack):
                    return False
                if(stack.pop()!=inp):
                    return False
        return len(stack)==0