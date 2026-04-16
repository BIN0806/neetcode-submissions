# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 and list2:
            ptr = list1 if (list1.val >= list2.val) else list2
        elif list1:
            ptr = list1
        elif list2:
            ptr = list2
        else:
            return None

        while list1:
            if list2:
                if list1.val <= list2.val:
                   temp = list1.next

                   list1.next = list2 
                   list2 = temp

                   list1 = list1.next
                else:
                   temp = list2.next

                   list2.next = list1
                   list1 = temp

                   list2 = list2.next
            else:
                return ptr
        if list2:
            ptr = list2
        return ptr