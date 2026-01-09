class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# longer solution
def delete_node(head, target):
    # edge case: since {prev = None} in the very beginning
    if head.val == target:
        return head.next

    prev = None
    curr = head

    while curr:
        if curr.val == target:
            prev.next = curr.next
            break
        prev = curr
        curr = curr.next

    return head


# using dummy node to make it simpler
def delete_node_better(head, target):
    dummy = ListNode(0)
    dummy.next = head
    prev = dummy
    curr = head
    while curr:
        if curr.val == target:
            prev.next = curr.next
            break
        prev = curr
        curr = curr.next
    return dummy.next


def fast_and_slow(head):
    fast = head
    slow = head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
    return slow
