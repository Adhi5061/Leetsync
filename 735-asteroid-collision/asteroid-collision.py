class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack=[]
        ind=0
        while(ind<len(asteroids)):
            i=asteroids[ind]
            if(stack):
                    ele=stack[-1]
                    if((ele>0 and i>0) or (ele<0 and i<0)):
                        stack.append(i)
                        ind+=1
                    else:
                        st=stack[-1]
                        if((i<0 and ele>0)):
                            if(abs(st)==abs(i)):
                                stack.pop()
                                ind+=1
                            elif(abs(st)>abs(i)):
                                ind+=1
                            else:
                                stack.pop()
                        else:
                            stack.append(i)
                            ind+=1
            else:
                stack.append(i)
                ind+=1               
        return stack