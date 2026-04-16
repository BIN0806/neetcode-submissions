# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        result = []
        def dfs(node, counter): # pre-order variant
            if not node: return 
            dfs(node.left, counter + 1)
            result.append(node.val)
            dfs(node.right, counter + 1)


            
        dfs(root, 0)
        print(result)
        return result[k-1]
