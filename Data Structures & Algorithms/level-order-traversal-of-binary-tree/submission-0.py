# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        from collections import deque
        result = []
        queue = deque([root])
        while queue:
            new_q = deque()
            node = queue.popleft()
            layer = []
            if node:
                layer.append(node.val)
                if node.left:  
                    new_q.append(node.left)
                if node.right: 
                    new_q.append(node.right)

            while queue:
                node = queue.popleft()
                layer.append(node.val)
                if node.left:  new_q.append(node.left)
                if node.right: new_q.append(node.right)

            print(layer)
            queue = new_q
            result.append(layer)
        return result

