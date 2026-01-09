class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 2 pointer solution (fast and slow)
# using Dummy Node is always easier
# this solution solves it in one pass, instead of calculating the length first
def remove_nth_from_end(head, n):
    dummy = ListNode(0)
    dummy.next = head

    # fast, slow = dummy, dummy
    fast = slow = dummy

    for _ in range(n):
        fast = fast.next

    while fast.next:
        fast = fast.next
        slow = slow.next

    # remove nth node from end
    slow.next = slow.next.next
    return dummy.next

# less optimal solution, which has 2 passes
# first pass to get the length
def removeNthFromEnd(head, n):
    # find length
    length = 0
    current = head
    while current:
        length += 1
        current = current.next

    target = length - n
    if target == 0:
        return head.next

    current = head
    for _ in range(target - 1):
        current = current.next

    current.next = current.next.next
    return head