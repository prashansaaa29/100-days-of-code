#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3
def insert(head, data):
    r=Node(data)
    r.npx=head
    return r
def getList(head):
    q=[]
    while head:
        q.append(head.data)
        head=head.npx
    return q

#{ 
 # Driver Code Starts.
#Back-end complete function Template for Python 3
class Node:
    def __init__(self, x):
        self.data = x
        self.npx = None

def XOR(a, b):
    return id(a) ^ id(b)


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        head = None
        data_list = list(map(int, input().split()))
        for data in data_list:
            head = insert(head, data)
        
        vec = getList(head)
        print(*vec)
        print(*reversed(vec))

# } Driver Code Ends