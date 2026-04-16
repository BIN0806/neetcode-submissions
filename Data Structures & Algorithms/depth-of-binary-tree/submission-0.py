# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    from collections import deque
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(cur_node, cur_len):
            if not cur_node:
                return 0 
            return max(dfs(cur_node.left, cur_len), dfs(cur_node.right, cur_len)) + 1
    
        return dfs(root, 1) if root else 0 
