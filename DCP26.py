#How to remove the Kth last element from the list in constant space and in one pass

#initialize Node structure
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

#functions removes the k-th to last index
def remove_k_fromLast(linkedList, k):
    first, second = linkedList, linkedList
    
    #moves up the head of the list by k
    for i in range(k):
        first = first.next

    prev = None

    #second will be in the position that we would want to remove
    while first:
        prev = second
        second = second.next
        first = first.next
    
    #skips the value of second
    prev.next = second.next


head = Node(1, Node(2, Node(3, Node(4, Node(5, Node(6))))))
remove_k_fromLast(head, 3)
print(head)