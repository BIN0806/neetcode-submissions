# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
        else:
            temp1, temp2 = root.left, root.right
            if root.left:
                root.left = self.invertTree(temp2)
            if root.right:
                root.right = self.invertTree(temp1)
        return root