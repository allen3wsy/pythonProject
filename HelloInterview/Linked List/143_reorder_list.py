from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return

        # Step 1: Find the middle of the list using slow/fast pointers
        slow = fast = head

        # Making sure slow is the left of the middle 2 nodes: [1,2,3,4]...
        # e.g: slow is at 2
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        # Step 2: Reverse the second half starting from slow.next
        second_half = self.reverse_list(slow.next)
        # E.g. don't forget to cut the list into two halves
        slow.next = None

        # Step 3: Merge two halves alternately
        first_half = head

        # second_half list is shorter or equal to first_half
        while second_half:
            first_next = first_half.next  # Store next for first_half list
            second_next = second_half.next # Store next for second_half list

            first_half.next = second_half  # Link first to second
            second_half.next = first_next  # Link second to first's next

            first_half = first_next  # Move to next nodes
            second_half = second_next

    def reverse_list(self, head):
        prev = None
        current = head

        while current:
            next_temp = current.next
            current.next = prev
            prev = current
            current = next_temp

        return prev
