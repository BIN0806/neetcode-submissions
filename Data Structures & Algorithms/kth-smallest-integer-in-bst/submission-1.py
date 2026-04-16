# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        result = []
        # def dfs(node): # pre-order variant
        #     if not node: return 
        #     dfs(node.left)
        #     result.append(node.val)
        #     dfs(node.right)
            
        # dfs(root)
        # return result[k-1]
        
        counter, cur = 0, root
        stack = []
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            counter += 1
            if counter == k:
                return cur.val
            cur = cur.right
        return -1
            