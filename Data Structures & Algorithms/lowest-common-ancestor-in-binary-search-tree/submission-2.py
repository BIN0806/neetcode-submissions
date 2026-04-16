# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        cur = root
        while cur:
            if p.val > cur.val and q.val > cur.val:
                cur = cur.right
            elif p.val < cur.val and q.val < cur.val:
                cur = cur.left
            else:
                return cur
                



        # num_to_depth = {}
        # num_to_depth[0] = {}
        # num_to_depth[1] = {}
        # # 

        # def dfs(node, num, height, which):
        #     if node:
        #         if not node.left and not node.right:
        #             num_to_depth[which][node.val] = height
        #         elif node.left and node.left.val < num:
        #             num_to_depth[which][node.left.val] = num
        #             return dfs(node.left, num, height + 1, which)
        #         elif node.right and node.right.val > num:
        #             num_to_depth[which][node.right.val] = num
        #             return dfs(node.right, num, height + 1, which)

        # dfs(root, p.val, 0, 0)
        # dfs(root, q.val, 0, 1)

        # lowest_depth = -1
        # lca_val = -1000
        # for p_depth, q_depth in zip(num_to_depth[0], num_to_depth[1]):
        #     if depth > lowest_depth and tup[0] == tup[1]: 
        #         depth = lowest_depth
        #         lca_val = tup[0]
        # return lca_val


