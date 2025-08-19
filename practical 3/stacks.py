class stack:
    def __init__(self):
        self.items = []
    def empty(self):
        return len(self.items) == 0
    def push(self, item):
        self.items.append(item)
    def pop(self):
        if not self.empty():
            return self.items.pop()
        else:
            raise IndexError("stack is empty")
    def peek(self):
        if not self.empty():
            return self.items[-1]
        else:
            raise IndexError("stack is empty")
    def size(self):
        return len(self.items)
# Test the Stack
stack = stack()
stack.push(1)
stack.push(2)
stack.push(3)
print(stack.pop()) 
print(stack.peek())  
print(stack.size())  