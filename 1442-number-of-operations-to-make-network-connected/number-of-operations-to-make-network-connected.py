class disjointset:
    def __init__(self,n):
        self.size=[1]*n
        self.parent=list(range(n))
    def find(self,x):
        if(self.parent[x]!=x):
            self.parent[x]=self.find(self.parent[x])
            return self.parent[x]
        return self.parent[x]
    def connected(self,x,y):
        return self.find(x)==self.find(y)
    def union(self,x,y):
        px=self.find(x)
        py=self.find(y)
        if(px!=py):
            if(self.size[px]>=self.size[py]):
                self.parent[py]=px
                self.size[px]+=self.size[py]
            elif(self.size[py]>self.size[px]):
                self.parent[px]=py
                self.size[py]+=self.size[px]

class Solution:
    def makeConnected(self, n: int, adj: List[List[int]]) -> int:
        d=disjointset(n)
        extra=0
        # for node in range(n):
        for start,end in adj:
            if(d.connected(start,end)):
                extra+=1
            else:
                d.union(start,end)
        components = sum(1 for i in range(n) if d.find(i) == i)
        
        # Number of operations needed to connect all components
        needed_operations = components - 1
        
        return needed_operations if needed_operations <= extra else -1