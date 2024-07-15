# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        d={}
        p=set()
        c=set()
        for n in descriptions:
            pnode=TreeNode(n[0])
            cnode=TreeNode(n[1])
            p.add(n[0])
            c.add(n[1])
            if(n[1] in d):
                if(n[0] in d):
                    if(n[2]):
                        d[n[0]].left=d[n[1]]
                    else:
                        d[n[0]].right=d[n[1]]
                else:
                    if(n[2]):
                        pnode.left=d[n[1]]
                    else:
                        pnode.right=d[n[1]]
                    d[n[0]]=pnode
            elif(n[0] in d):
                if(n[2]):
                    d[n[0]].left=cnode
                else:
                    d[n[0]].right=cnode
                d[n[1]]=cnode
            else:
                if(n[2]):
                    pnode.left=cnode                
                else:
                    pnode.right=cnode
                d[n[0]]=pnode
                d[n[1]]=cnode
        # //print(list((p-c))[0])
        return d[list(p-c)[0]]