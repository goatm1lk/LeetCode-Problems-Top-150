import random

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Create a linked list of random numbers to reverse
dummy = ListNode(0)
curr = dummy
for _ in range(10):
    curr.next = ListNode(random.randint(1, 100))
    curr = curr.next

LinkedListOfRandomNums = dummy.next

# Create a copy of the linked list
LinkedListOfRandomNumsCopy = ListNode(0)
reversed_curr = LinkedListOfRandomNumsCopy
original_curr = LinkedListOfRandomNums

# Iterate through the original list to create a copy with reversed order
while original_curr:
    # Assign the value of the next node in the copy list to be equal to the original value in the first list.
    reversed_curr.next = ListNode(original_curr.val)
    # Move to the next node you had just assigned the value to.
    reversed_curr = reversed_curr.next
    # Move the original list to the next node as well.
    original_curr = original_curr.next

# Store a reference to the head of the reversed list for further processing.
original_list = LinkedListOfRandomNumsCopy.next

# Function to reverse the linked list
def reverseLinkedList(head):
    prev, curr = None, head
    # Iterate through the whole head of integers.
    while head:
        # Hold the next cell in a temp variable.
        temp = head.next
        # Reverse the pointer for the current cell by setting it to the previous cell.
        head.next = prev
        # Then move the list along, set prev to head, and head to the temp variable.
        prev, head = head, temp
    # Return Prev as the starting head
    return prev

result = reverseLinkedList(LinkedListOfRandomNums)

print("\nOriginal List:")
while original_list:
    print(original_list.val)
    original_list = original_list.next

print("\nList of Reversed Numbers:")
while result:
    print(result.val)
    result = result.next
