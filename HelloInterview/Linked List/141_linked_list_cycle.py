class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# fast and slow pointer
# O(N) time but O(1) space
# edge case:
# - single node
# - single node (pointing to itself)
# - empty list
def has_cycle(head):
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False


# using set()
# O(N) time and O(N) space
def has_cycle_2(head):
    visited_nodes = set()

    curr = head

    while curr:
        if curr in visited_nodes:
            return True

        visited_nodes.add(curr)
        curr = curr.next

    return False
