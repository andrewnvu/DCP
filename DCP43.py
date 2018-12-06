#implement a stack with the following methods
#push(val) - pushes an element onto the stack
#pop() - pops off and returns top element of stack
#           if no elements in stack, then throw error or return null
#max() - returns max value in stack
#           if no elements in the stack, then throw an error or return null



class Stack:
    def __init__(self):
        self.items = []

    def push(self, val):
        self.items.append(val)

    def pop(self):
        if not self.is_empty():
            self.items.pop()
        else:
            print("There is nothing to pop")

    def peek(self):
        return self.items[-1]

    def is_empty(self):
        return self.items == []

    def max(self):
        if not self.is_empty():
            return max(self.items)
        else:
            return None

    def get_items(self):
        return self.items

s = Stack()

print(s.is_empty())
s.push(1)
s.push(2)
print(s.max())
s.pop()
print(s.max())
s.pop()
print(s.max())
s.pop()
s.push(2)
s.push(1)
s.push(3)
s.push(4)

print(s.get_items())
print(s.peek())

s.pop()
s.pop()
print(s.get_items())

print(s.peek())