# Hint: using 2 dummy nodes
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        # before and after are the two pointers used to create two list
        # before_dummy and after_dummy are used to save the heads of the two lists.
        # All of these are initialized with the dummy nodes created.
        before = before_dummy = ListNode(0)
        after = after_dummy = ListNode(0)

        while head:
            # If the original list node is lesser than the given x,
            # assign it to the before list.
            if head.val < x:
                before.next = head
                before = before.next
            else:
                # If the original list node is greater or equal to the given x,
                # assign it to the after list.
                after.next = head
                after = after.next

            # move ahead in the original list
            head = head.next

        # EX: its easy to forget this line...
        # Last node of "after" list would also be ending node of the reformed list
        # e.g. from Original list: 1->5->10->1. and x=3 then '10'->'1' so I have to set '10'->None
        after.next = None

        # Once all the nodes are correctly assigned to the two lists,
        # combine them to form a single list which would be returned.
        before.next = after_dummy.next

        return before_dummy.next