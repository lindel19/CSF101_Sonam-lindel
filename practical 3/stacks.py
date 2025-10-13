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
#Exercise 
#1.Implement a function that uses a stack to evaluate postfix expressions.
def evaluate_postfix(expression):
    stack = []
    for token in expression.split():
        if token.isdigit():
            stack.append(int(token))
        else:
            b = stack.pop()
            a = stack.pop()
            if token == '+':
                stack.append(a + b)
            elif token == '-':
                stack.append(a - b)
            elif token == '*':
                stack.append(a * b)
            elif token == '/':
                stack.append(a / b)
    return stack[0]
#2.Create a function that uses two stacks to implement a queue

