"""
# Practical 6 Reflection: Implementing Stack and Queue Operations in Python

# Objective Reflection:
 I implemented key stack and queue operations in Python, including:
- Evaluating postfix expressions using a stack
- Implementing a queue using two stacks
- Creating a basic task scheduler using a queue
- Converting infix expressions to postfix using a stack

# The main objective was to understand how these fundamental data structures work,
analyze their utility in solving practical problems, and learn how to manipulate
data efficiently using stacks and queues.

# What I Learned:

# 1. Postfix Evaluation Using Stack
   - A stack provides a natural way to evaluate postfix expressions.
   - Operations are performed in the order of encountering operators after operands.
   - Learned the importance of order of operations and how a stack maintains the correct execution sequence.

2. Queue Using Two Stacks
   - Implementing a queue with two stacks illustrated data structure transformations.
   - Learned how enqueue operations push into one stack while dequeue operations pop from the other.
   - Gained insight into amortized efficiency—multiple enqueues can be cheap, but occasional stack transfers are necessary for FIFO behavior.

# 3. Task Scheduler Using Queue
   - Using a queue to schedule tasks emphasized the FIFO property in real-world applications.
   - Learned how simple data structures can implement practical systems like job scheduling or process management.
   - Processing tasks sequentially reinforced how queues manage order and fairness.

# 4. Infix-to-Postfix Conversion Using Stack
   - Learned the shunting-yard algorithm to handle operator precedence and parentheses.
   - Reinforced the idea that stacks are ideal for problems requiring last-in-first-out (LIFO) access.
   - Understanding how to manage operator precedence and associativity was a key insight.

# Challenges Faced:
- Maintaining correct operator precedence in the infix-to-postfix conversion initially caused errors.
- Ensuring queue operations using two stacks were efficient required careful thought about when to transfer elements between stacks.
- Handling invalid input or malformed expressions in postfix evaluation required defensive programming to avoid runtime errors.
- Designing a task scheduler that could handle dynamic tasks in FIFO order while being easy to extend for more complex use cases.

# Conclusion:
This  strengthened my understanding of stacks and queues, demonstrating their practical applications
in expression evaluation, scheduling, and data structure implementation. I now appreciate:
- How stacks simplify problems that require reversing order or keeping track of recent elements.
- How queues manage sequential processing in real-world scenarios.
- How implementing these data structures in Python reinforces algorithmic thinking and problem-solving skills.


