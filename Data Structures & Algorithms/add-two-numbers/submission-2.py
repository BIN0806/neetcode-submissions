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

        carry = False
        while ptr1 or ptr2:
            val = 0
            val += ptr1.val if ptr1 else 0
            val += ptr2.val if ptr2 else 0 
            if carry:
                val += 1
                carry = False
            if val >= 10:
                carry = True

            dummyPtr.next = ListNode(val % 10)

            ptr1 = ptr1.next if ptr1 else None
            ptr2 = ptr2.next if ptr2 else None
            dummyPtr = dummyPtr.next
            
        if carry: dummyPtr.next = ListNode(1)
            
        return dummy.next