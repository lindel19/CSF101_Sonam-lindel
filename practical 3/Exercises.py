#Exercise 
# 1. Evaluate Postfix Expression using Stack
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


# 2. Implement Queue using Two Stacks
class TwoStackQueue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, value):
        self.stack1.append(value)

    def dequeue(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        if not self.stack2:
            raise IndexError("Queue is empty")
        return self.stack2.pop()

    def is_empty(self):
        return not (self.stack1 or self.stack2)


# 3. Task Scheduler using Queue
class TaskScheduler:
    def __init__(self):
        self.queue = TwoStackQueue()

    def add_task(self, task):
        self.queue.enqueue(task)

    def process_tasks(self):
        while not self.queue.is_empty():
            task = self.queue.dequeue()
            print(f"Processing task: {task}")


# 4. Convert Infix Expression to Postfix using Stack
def infix_to_postfix(expression):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    stack = []
    output = []

    for token in expression.split():
        if token.isalnum():
            output.append(token)
        elif token == '(':
            stack.append(token)
        elif token == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()  # Remove '('
        else:
            while (stack and stack[-1] != '(' and
                   precedence.get(token, 0) <= precedence.get(stack[-1], 0)):
                output.append(stack.pop())
            stack.append(token)

    while stack:
        output.append(stack.pop())

    return ' '.join(output)

# Main block to run examples

if __name__ == "__main__":
    print("=== Postfix Evaluation ===")
    print(evaluate_postfix("3 4 + 2 * 7 /"))  

    print("\n=== Queue using Two Stacks ===")
    q = TwoStackQueue()
    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)
    print("Dequeued:", q.dequeue())  
    print("\n=== Task Scheduler ===")
    scheduler = TaskScheduler()
    scheduler.add_task("Task 1")
    scheduler.add_task("Task 2")
    scheduler.process_tasks()  

    print("\n=== Infix to Postfix ===")
    print(infix_to_postfix("( A + B ) * C - D"))  
