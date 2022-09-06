class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


a = Node('A')
b = Node('B')
c = Node('C')
d = Node('D')

a.next = b
b.next = c
c.next = d

# A -> B -> C -> D -> None


# Iterative
# def print_list(head):
#     current = head
#     while current is not None:
#         print(current.val)
#         current = current.next

# Recursive
set_num = set()

set_num.add(5)
set_num.add(6)
set_num.add(6)
set_num.add(6)

print(set_num)
print(len(set_num))