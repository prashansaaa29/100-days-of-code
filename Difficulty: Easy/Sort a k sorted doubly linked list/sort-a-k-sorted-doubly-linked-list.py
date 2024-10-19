#User function Template for python3
'''
class DLLNode:
    def __init__(self,val) -> None:
        self.data = val
        self.prev = None
        self.next = None
'''
import heapq

class DLLNode:
    def __init__(self, val) -> None:
        self.data = val
        self.prev = None
        self.next = None

class Solution:
    def sortAKSortedDLL(self, head, k):
        if not head:
            return None

        # Min-Heap to store the elements
        min_heap = []
        
        # Initialize the current node and new head for sorted list
        current = head
        new_head = None
        new_tail = None

        # Add first k+1 elements to the heap
        for i in range(k + 1):
            if current:
                heapq.heappush(min_heap, current.data)
                current = current.next

        # Process the remaining nodes
        while min_heap:
            # Get the smallest element from the heap
            smallest_value = heapq.heappop(min_heap)
            # Create a new node with the smallest value
            new_node = DLLNode(smallest_value)

            # If this is the first node being added to the new list
            if not new_head:
                new_head = new_node
                new_tail = new_node
            else:
                new_tail.next = new_node
                new_node.prev = new_tail
                new_tail = new_node
            
            # Add the next node from the original list to the heap
            if current:
                heapq.heappush(min_heap, current.data)
                current = current.next
        
        # Link back to the head of the new list
        new_head.prev = None  # Head should not have a previous node

        return new_head

        # Code Here


#{ 
 # Driver Code Starts
import heapq


# A node of the doubly linked list
class DLLNode:

    def __init__(self, val):
        self.data = val
        self.next = None
        self.prev = None


# Function to insert a node at the end of the doubly linked list
def push(tail, new_data):
    new_node = DLLNode(new_data)
    new_node.next = None
    new_node.prev = tail

    if tail is not None:
        tail.next = new_node

    return new_node


# Function to print nodes in a given doubly linked list
def printList(head):
    while head is not None:
        print(head.data, end=" ")
        head = head.next
    print()


# Driver code
if __name__ == "__main__":
    t = int(input())  # Number of test cases
    for _ in range(t):
        arr = list(map(int, input().split()))  # Read the input array
        k = int(input())  # Read the value of k

        head = DLLNode(arr[0])
        tail = head

        for i in range(1, len(arr)):
            tail = push(tail, arr[i])

        solution = Solution()
        sorted_head = solution.sortAKSortedDLL(head, k)
        printList(sorted_head)

# } Driver Code Ends