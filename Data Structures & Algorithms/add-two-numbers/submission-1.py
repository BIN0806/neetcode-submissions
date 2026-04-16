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
        while ptr1 and ptr2:
            val = ptr1.val + ptr2.val
            if carry:
                val += 1
                carry = False
            if val >= 10:
                carry = True

            dummyPtr.next = ListNode(val % 10)

            ptr1, ptr2 = ptr1.next, ptr2.next
            dummyPtr = dummyPtr.next
            
        while ptr1:
            val = ptr1.val
            if carry:
                val += 1
                carry = False
            if val >= 10:
                carry = True
            dummyPtr.next = ListNode(val % 10)
            ptr1 = ptr1.next
            dummyPtr = dummyPtr.next
        while ptr2:
            val = ptr2.val
            if carry:
                val += 1
                carry = False
            if val >= 10:
                carry = True
            dummyPtr.next = ListNode(val % 10)
            ptr2 = ptr2.next
            dummyPtr = dummyPtr.next

        if carry: dummyPtr.next = ListNode(1)
            
        return dummy.next