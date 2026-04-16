# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        balanced = True
        def dfs(node):
            nonlocal balanced
            if not node: return 0 

            left_height = dfs(node.left)
            right_height = dfs(node.right)
            print("cur:", node.val, left_height, right_height)
            if not(1 + left_height == right_height or 
                1 + right_height == left_height or
                left_height == right_height):
                balanced = False
                print("conditioned not satisfied") 
            print(balanced)
            return max(left_height, right_height) + 1
        dfs(root)
        print(balanced)
        return balanced