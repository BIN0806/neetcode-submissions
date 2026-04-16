"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        old_to_copy = {None: None}

        ptr = head
        while ptr:
            copy = Node(ptr.val)
            old_to_copy[ptr] = copy
            ptr = ptr.next

        ptr = head
        while ptr:
            copy_node = old_to_copy[ptr]
            copy_node.next = old_to_copy[ptr.next]
            copy_node.random = old_to_copy[ptr.random]
 
            ptr = ptr.next

        return old_to_copy[head]