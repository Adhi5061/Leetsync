# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        from collections import deque
        q=deque()
        q.append((root,0))
        d={}
        depth=0
        while(q):
            for t in range(len(q)):
                node,level=q.popleft()
                if(level in d):
                    if(depth in d[level]):
                        d[level][depth].append(node.val)
                    else:
                        d[level][depth]=[node.val]
                else:
                    d[level]={}
                    d[level][depth]=[node.val]
                if(node.left):
                    q.append((node.left,level-1))
                if(node.right):
                    q.append((node.right,level+1))
            depth+=1
        # print(d)
        d=dict(sorted(d.items()))
        res=[]
        # print(d)
        for key,val in d.items():
            temp=[]
            for key2,val2 in val.items():
                temp.extend(sorted(val2))
            res.append(temp)
        return res