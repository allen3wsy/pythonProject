class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# better and simpler solution
# no need to find the HEAD like the solution below
def merge_two_lists(l1, l2):
    dummy = ListNode()
    tail = dummy # tail can also be called curr(ent)
    while l1 and l2:
        if l1.val < l2.val:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next
    tail.next = l1 or l2
    return dummy.next


# more complex (not recommended)
def merge_lists(l1, l2):
    # 1) the edge case
    if not l1: return l2
    if not l2: return l1

    # 2) the setup !!! setting the HEAD
    if l1.val < l2.val:
        head = l1
        l1 = l1.next
    else:
        head = l2
        l2 = l2.next

    # 3) start the while loop: defining current pointer
    current = head
    while l1 and l2:
        if l1.val < l2.val:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next
        current = current.next
    current.next = l1 or l2
    return head

