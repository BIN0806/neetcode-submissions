# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head
        while fast:
            if slow == fast:
                return True
            fast = fast.next
            slow = slow.next if slow else None
            if fast:
                fast = fast.next
            else:
                return True
        return False