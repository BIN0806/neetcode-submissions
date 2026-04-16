# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    from collections import deque
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # def dfs(cur_node, cur_len):
        #     if not cur_node:
        #         return 0 
        #     return max(dfs(cur_node.left, cur_len), dfs(cur_node.right, cur_len)) + 1
        # return dfs(root, 1) if root else 0 

        if not root:
            return 0 
        max_len, queue, = 1, deque([(root, 1)]) 
        while queue:
            cur_node, cur_len = queue.popleft()
            max_len = max(max_len, cur_len)

            if cur_node.left or cur_node.right:
                if cur_node.left:
                    queue.append((cur_node.left, cur_len + 1))
                if cur_node.right:
                    queue.append((cur_node.right, cur_len + 1))
            print(cur_node.val, cur_len, queue)

        return max_len

