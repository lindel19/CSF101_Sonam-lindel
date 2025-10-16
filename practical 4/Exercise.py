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

# LeetCode Problem 1: Reverse Linked List
def reverseList(head):
    prev = None
    current = head
    
    while current:
        next_temp = current.next
        current.next = prev
        prev = current
        current = next_temp
    
    return prev

# LeetCode Problem 2: Merge Two Sorted Lists
def mergeTwoLists(list1, list2):
    dummy = ListNode(0)
    current = dummy
    
    while list1 and list2:
        if list1.val <= list2.val:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next
        current = current.next
    
    if list1:
        current.next = list1
    if list2:
        current.next = list2
    
    return dummy.next

# LeetCode Problem 3: Remove Nth Node From End of List
def removeNthFromEnd(head, n):
    dummy = ListNode(0)
    dummy.next = head
    fast = slow = dummy
    
    for _ in range(n):
        fast = fast.next
    
    while fast.next:
        fast = fast.next
        slow = slow.next
    
    slow.next = slow.next.next
    
    return dummy.next

# ListNode class for LeetCode problems
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Helper function to create linked list from list
def create_linked_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

# Helper function to convert linked list to list
def linked_list_to_list(head):
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result

# Test the implementations
if __name__ == "__main__":
    print("Testing LinkedList implementation:")
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.append(4)
    ll.append(5)
    ll.print_list()
    
    print("\nTesting reverse method:")
    ll.reverse()
    ll.print_list()
    
    print("\nTesting find_middle method:")
    print("Middle element:", ll.find_middle())
    
    print("\nTesting has_cycle method:")
    print("Has cycle:", ll.has_cycle())
    
    print("\nTesting remove_duplicates method:")
    ll_with_duplicates = LinkedList()
    ll_with_duplicates.append(1)
    ll_with_duplicates.append(2)
    ll_with_duplicates.append(2)
    ll_with_duplicates.append(3)
    ll_with_duplicates.append(4)
    ll_with_duplicates.append(4)
    ll_with_duplicates.append(4)
    ll_with_duplicates.append(5)
    print("Before removing duplicates:")
    ll_with_duplicates.display()
    ll_with_duplicates.remove_duplicates()
    print("After removing duplicates:")
    ll_with_duplicates.display()
    
    print("\nTesting merge_sorted_lists method:")
    list1 = LinkedList()
    list1.append(1)
    list1.append(3)
    list1.append(5)
    
    list2 = LinkedList()
    list2.append(2)
    list2.append(4)
    list2.append(6)
    
    print("List 1:")
    list1.display()
    print("List 2:")
    list2.display()
    
    merged = list1.merge_sorted_lists(list2)
    print("Merged list:")
    merged.display()
    
    print("\nTesting LeetCode problems:")
    
    # Test Reverse Linked List
    head = create_linked_list([1, 2, 3, 4, 5])
    reversed_head = reverseList(head)
    print("Reverse Linked List:", linked_list_to_list(reversed_head))
    
    # Test Merge Two Sorted Lists
    list1 = create_linked_list([1, 2, 4])
    list2 = create_linked_list([1, 3, 4])
    merged = mergeTwoLists(list1, list2)
    print("Merge Two Sorted Lists:", linked_list_to_list(merged))
    
    # Test Remove Nth Node From End of List
    head = create_linked_list([1, 2, 3, 4, 5])
    result = removeNthFromEnd(head, 2)
    print("Remove Nth Node From End of List:", linked_list_to_list(result))