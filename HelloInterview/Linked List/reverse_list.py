# worth writing it out and plug it in whenever needed
def reverse(head):
    prev = None
    current = head
    while current:
        next_ = current.next
        current.next = prev
        prev = current
        current = next_
    return prev
