# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        list1, current = [], self
        while current:
            list1.append(str(current.val))
            current = current.next
        return "->".join(list1)

class Solution:
    def reverse(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = None
        while head:
            temp = head.next
            head.next = dummy
            dummy = head
            head = temp
        return dummy

    def reorderList(self, head: Optional[ListNode]) -> None:
        # Set Slow.next to Middle
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Reverse Second_Half
        left_ptr, right_ptr = head, self.reverse(slow.next)
        slow.next = None
        while right_ptr:
    #   Basically insert the 2nd list element into left_ptr and left_ptr.next
            temp1, temp2 = left_ptr.next, right_ptr.next 
            left_ptr.next = right_ptr
            right_ptr.next = temp1
            left_ptr, right_ptr = temp1, temp2


        # [1, 2,| 3, 4]
        # [1, 2,| 4, 3]
        # [1, 4,| 2, 3]

        # [1, 2, | 3, 4, 5]
        # [1, 2, | 5, 4, 3]
        # [1, 5, 2, 4, 3]
