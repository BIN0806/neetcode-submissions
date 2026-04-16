# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        ptr, slow, fast = head, head, head
        for _ in range(n):
            if fast:
                fast = fast.next 
            else:
                slow.next = None
                ptr.next = slow.next
                return head
                
        print(fast, slow.val, ptr.val)
        while fast:
            fast = fast.next 
            ptr = slow
            slow = slow.next

        print(fast, slow.val, ptr.val)
        ptr.next = slow.next
        slow.next = None

        return head

