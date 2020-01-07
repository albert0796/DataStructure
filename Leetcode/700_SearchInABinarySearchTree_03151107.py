
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
class Solution:
    def searchBST(self, root, val: int):
        if root == None:
            return
        
        if root.val == val:
            return root
        
        elif val < root.val:
            return self.searchBST(root.left, val)
        
        elif val > root.val:
            return self.searchBST(root.right, val)
        
        