# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ptr1, ptr2 = l1, l2
        dummy = ListNode(-1)
        dummyPtr = dummy

        running_total = 0
        while ptr1 or ptr2:
            running_total += ptr1.val if ptr1 else 0
            running_total += ptr2.val if ptr2 else 0 

            node_val = running_total - running_total // 10
            running_total = running_total // 10                
            dummyPtr.next = ListNode(node_val % 10)

            ptr1 = ptr1.next if ptr1 else None
            ptr2 = ptr2.next if ptr2 else None
            dummyPtr = dummyPtr.next
            
        if carry: dummyPtr.next = ListNode(1)
            
        return dummy.next