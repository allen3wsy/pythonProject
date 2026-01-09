# 3. Optimal Solution: Reverse Second Half
def is_palindrome(head):
    # 1) Find middle of the linked list using fast and slow pointers
    slow = fast = head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
    # 2) Reverse second half of the list
    curr, prev = slow, None
    while curr:
        next_ = curr.next  # Save next node
        curr.next = prev   # Reverse pointer
        prev = curr        # Move pointers
        curr = next_
    # 3) Check palindrome by comparing halves
    left, right = head, prev
    while right:
        if left.val != right.val:
            return False
        left = left.next
        right = right.next
    return True

# Solution 1. Convert to List: Compare Reverse
def is_palindrome_1(head):
    # convert linked list to list
    vals = []
    current_node = head
    while current_node:
        vals.append(current_node.val)
        current_node = current_node.next

    # compare list with its reverse
    return vals == vals[::-1]

# Solution 2. Convert to List: Two-Pointer Technique
def is_palindrome_2(head):
    # convert linked list to list
    vals = []
    current = head
    while current:
        vals.append(current.val)
        current = current.next

    left, right = 0, len(vals) - 1
    while left < right:
        if vals[left] != vals[right]:
            return False
        left, right = left + 1, right - 1

    return True