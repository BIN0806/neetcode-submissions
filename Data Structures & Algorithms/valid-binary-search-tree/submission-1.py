# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, l_val, r_val):
            if not node: return True
            if l_val < node.val < r_val:
                return dfs(node.left, l_val, node.val) and  dfs(node.right, node.val, r_val)
            return False
        return dfs(root, -float('inf') , float('inf'))