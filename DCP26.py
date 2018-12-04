# This problem was asked by Google.

# Given a singly linked list and an integer k, remove the kth last element from the list. 
# k is guaranteed to be smaller than the length of the list.

# The list is very long, so making more than one pass is prohibitively expensive.

# Do this in constant space and in one pass



class Node:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next

    def __str__(self):
        current_node = self
        result = []

        while current_node:
            result.append(current_node.val)
            current_node = current_node.next

        return str(result)


def remove(linkedList, k):
    first, second = linkedList, linkedList
    
    for i in range(k):
        first = first.next

    prev = None

    while first:
        prev = second
        second = second.next
        first = first.next

    prev.next = second.next


head = Node(1, Node(2, Node(3, Node(4, Node(5, Node(6))))))
remove(head, 3)
print(head)