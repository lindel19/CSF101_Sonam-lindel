class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    # Insert a new node at the end
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

# 1. Find the middle element
    def find_middle(self):
        slow = self.head#uses two pointers: slow moves one step, fast moves two steps.
        fast = self.head#When fast reaches the end, slow is at the middle.
        if not self.head:
            return None
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow.data

# 2. Detect cycle using Floyd’s Tortoise and Hare
    def has_cycle(self):#Uses Floyd's Tortoise and Hare algorithm in which slow moves one step and fast moves two steps 
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

# 3. Remove duplicates from unsorted linked list
    def remove_duplicates(self): #Remove_duplicates method uses a set to track seen values and removes any duplicate nodes by adjusting pointers
        current = self.head
        prev = None
        seen = set()
        while current:
            if current.data in seen:
                prev.next = current.next  # skip duplicate node
            else:
                seen.add(current.data)
                prev = current
            current = current.next

# 4. Merge two sorted linked lists (static method)
    @staticmethod #a static method is a method that belongs to a class but does not require an instance to be called
    def merge_sorted(list1, list2): #Merges two sorted linked lists into a single sorted linked list by comparing nodes from both lists and linking them in order
        dummy = Node(0) #dummy node to simplify edge cases
        tail = dummy
        a = list1.head
        b = list2.head

        while a and b:
            if a.data < b.data:
                tail.next = a
                a = a.next
            else:
                tail.next = b
                b = b.next
            tail = tail.next

        tail.next = a if a else b
        merged_list = LinkedList()
        merged_list.head = dummy.next
        return merged_list

    # Helper: print linked list
    def print_list(self):
        current = self.head
        elements = []
        while current:
            elements.append(str(current.data))
            current = current.next
        print(" -> ".join(elements))


ll = LinkedList()
for value in [3, 5, 7, 5, 9, 3]:
    ll.append(value)

print("Original list:")
ll.print_list()

# Find middle
print("Middle element:", ll.find_middle())

# Remove duplicates
ll.remove_duplicates()
print("After removing duplicates:")
ll.print_list()

# Detect cycle
print("Has cycle?", ll.has_cycle())

# Merge two sorted linked lists
ll1 = LinkedList()
ll2 = LinkedList()
for v in [1, 3, 5]:
    ll1.append(v)
for v in [2, 4, 6]:
    ll2.append(v)

merged = LinkedList.merge_sorted(ll1, ll2)
print("Merged sorted list:")
merged.print_list()
