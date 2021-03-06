#!/usr/bin/python3
"""
Write a function, is_univalue_list, that takes in the head of a linked list as an argument. The function should return a boolean indicating whether or 
not the linked list contains exactly one unique value.

You may assume that the input list is non-empty.
"""
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

# Iterative
def is_univalue_list(head):
    # Time:
    # Space:
    current = head
    while current is not None:
        if head.val != current.val:
            return False
        current = current.next
    return True

# Recursive
def is_univalue_list(head, prev_val = None):
    # Time:
    # Space:
    if head is None:
        return True
    if prev_val is None or head.val == prev_val:
        return is_univalue_list(head.next, head.val)
    else:
        return False

# test_00:
a = Node(7)
b = Node(7)
c = Node(7)
a.next = b
b.next = c
# 7 -> 7 -> 7
assert(is_univalue_list(a) == True)
# test_01:
a = Node(7)
b = Node(7)
c = Node(4)
a.next = b
b.next = c
# 7 -> 7 -> 4
assert(is_univalue_list(a) == False)
# test_02:
u = Node(2)
v = Node(2)
w = Node(2)
x = Node(2)
y = Node(2)
u.next = v
v.next = w
w.next = x
x.next = y
# 2 -> 2 -> 2 -> 2 -> 2
assert(is_univalue_list(u) == True)
# test_03:
u = Node(2)
v = Node(2)
w = Node(3)
x = Node(3)
y = Node(2)
u.next = v
v.next = w
w.next = x
x.next = y
# 2 -> 2 -> 3 -> 3 -> 2
assert(is_univalue_list(u) == False)
# test_04:
z = Node('z')
# z
assert(is_univalue_list(z) == True)

print('-- Yay test completed!')
