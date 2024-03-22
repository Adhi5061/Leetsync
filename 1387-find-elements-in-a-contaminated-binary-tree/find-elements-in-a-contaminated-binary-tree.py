# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        self.root=root
        self.set=set()
        def dfs(root,curr):
            if(root==None):
                return 
            root.val=curr
            self.set.add(curr)
            dfs(root.left,curr*2+1)
            dfs(root.right,curr*2+2)
        dfs(self.root,0)

    def find(self, target: int) -> bool:
        return target in self.set
# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)