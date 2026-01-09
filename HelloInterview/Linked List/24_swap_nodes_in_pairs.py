class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# make sure to use Dummy node
def swap_pairs(head):
    dummy = ListNode(0)
    dummy.next = head
    prev, first = dummy, head

    while first and first.next:
        second = first.next

        # swap nodes
        prev.next = second
        first.next = second.next
        second.next = first

        prev = first
        first = first.next

    return dummy.next