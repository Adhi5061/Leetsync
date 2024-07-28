class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack=[]
        for ast in asteroids:
            flag=True
            while(stack and stack[-1]>0 and ast<0):
                flag=False
                if(abs(ast)==abs(stack[-1])):
                    stack.pop()
                    break
                if(abs(ast)<abs(stack[-1])):
                    break
                else:
                    flag=True
                    stack.pop()
            if(flag):
                stack.append(ast)
        return stack