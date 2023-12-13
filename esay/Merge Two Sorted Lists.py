# Definition for singly-linked list.
from typing import Optional

class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # 1. Create a dummy node
        dummy = ListNode()
        # 2. Create a pointer to the dummy node
        dummy_head = dummy

        while list1 is not None and list2 is not None:
            if list1.val < list2.val:
                dummy_head.next = list1
                list1 = list1.next
                print(dummy.val,end='->')
            else:
                dummy_head.next = list2
                list2 = list2.next
                print(dummy.val,end='->')

            dummy_head = dummy_head.next
            # If one list is longer than the other
        if list1 is not None:
            dummy_head.next = list1
        else:
            dummy_head.next = list2

        return dummy.next






if __name__ == "__main__":
        solution = Solution()
        list1 = ListNode(1, ListNode(2, ListNode(4)))
        list2 = ListNode(1, ListNode(3, ListNode(4)))
        solution.mergeTwoLists(list1, list2)