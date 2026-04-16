# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def dfs(node, biggest_val) -> int:
            if not node: return 0 
            count = 0
            if node.val >= biggest_val: count += 1
            print("node pre:", node.val)
            print("pre:", count)
            if node.left: count += dfs(node.left, max(biggest_val, node.val))
            print("pos left:", count)
            if node.right: count += dfs(node.right, max(biggest_val, node.val))
            print("pos right:", count)
            print("node post:", node.val)
            return count

        return dfs(root, -float('inf'))