import random

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Function to create a linked list of random numbers
def create_linked_list(length):
    dummy = ListNode(0)
    curr = dummy
    for _ in range(length):
        curr.next = ListNode(random.randint(1, 100))
        curr = curr.next
    return dummy.next

# Function to create a copy of a linked list
def copy_linked_list(head):
    dummy = ListNode(0)
    reversed_curr = dummy
    original_curr = head
    while original_curr:
        reversed_curr.next = ListNode(original_curr.val)
        reversed_curr = reversed_curr.next
        original_curr = original_curr.next
    return dummy.next

# Function to reverse a linked list between left and right indices
def ReverseLinkedListII_206(head, left, right):
    dummy = ListNode(next=head)
    left_prev, curr = dummy, head
    for _ in range(left - 1):
        left_prev = curr
        curr = curr.next
    prev = None
    for _ in range(right - left + 1):
        temp = curr.next
        curr.next = prev
        prev, curr = curr, temp
    left_prev.next.next = curr
    left_prev.next = prev
    return dummy.next

# Create a linked list of random numbers
LinkedListOfRandomNums = create_linked_list(10)

# Create a copy of the linked list
LinkedListOfRandomNumsCopy = copy_linked_list(LinkedListOfRandomNums)

# Store a reference to the head of the reversed list for further processing.
original_list = LinkedListOfRandomNumsCopy

# Generate random indices for reversing
rightValue = random.randint(1, 9) 
leftValue = random.randint(0, rightValue - 1)

# Reverse the linked list between left and right indices
result = ReverseLinkedListII_206(LinkedListOfRandomNums, leftValue, rightValue)

# Print the original list
print("\nOriginal List:")
while original_list:
    print(original_list.val)
    original_list = original_list.next

# Print the reversed list with indication of reversed section
print("\nList with Numbers Reversed:")
counter = 1
current = result
while current:
    if leftValue <= counter <= rightValue:
        print(current.val, "*", "Left", leftValue, "Right:", rightValue)
    else:
        print(current.val)
    current = current.next
    counter += 1
