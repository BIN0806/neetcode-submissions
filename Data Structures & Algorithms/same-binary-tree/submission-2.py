# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        from collections import deque
        q2 = deque([p])
        q1 = deque([q])
        if p and q:
            if p.val != q.val:
                return False
        else:
            if not q and not p:
                return True
            else:
                return False
        def compare(list_node1, list_node2):
            if len(list_node1) != len(list_node2):
                return False
            n = len(list_node1)
            for i in range(n):
                if list_node1[i] == None or list_node2[i] == None:
                    if list_node1[i] != list_node2[i]:
                        return False
                elif list_node1[i].val != list_node2[i].val:
                    return False
            return True

        while q1 or q2:
            node1 = q1.popleft()
            if (node1 != None):
                if node1.left: 
                    q1.append(node1.left)
                else:
                    q1.append(None)
                if node1.right: 
                    q1.append(node1.right)
                else:
                    q1.append(None)

            node2 = q2.popleft()
            if (node2 != None):
                if node2.left: 
                    q2.append(node2.left)
                else:
                    q2.append(None)
                if node2.right: 
                    q2.append(node2.right)
                else:
                    q2.append(None)
            print(q1)
            print(q2)                 
            if not compare(q1, q2):
               return False

        return q1 == q2
            
