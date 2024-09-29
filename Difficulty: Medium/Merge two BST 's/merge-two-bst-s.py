#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3
class GeneratorWrapper:
    def __init__(self, generator):
        self.generator = generator
        self._buffer = None
        self._exhausted = False
        self._prime()

    def _prime(self):
        if not self._exhausted and self._buffer is None:
            try:
                self._buffer = next(self.generator)
            except StopIteration:
                self._buffer = None
                self._exhausted = True

    def has_next(self):
        return not self._exhausted

    def get_next(self):
        if self._exhausted:
            raise StopIteration("No more elements in the generator")
        result = self._buffer
        self._buffer = None
        self._prime()
        return result

    def peek_next(self):
        if self._exhausted:
            raise StopIteration("No more elements in the generator")
        return self._buffer

class Solution:
    def merge(self, root1, root2):
        # code here
        # need to use generators for root1 and root2 and access them on demand
        gen1 = GeneratorWrapper(self.dfs(root1))
        gen2 = GeneratorWrapper(self.dfs(root2))
        
        ans = []
        while gen1.has_next() and gen2.has_next():
            if gen1.peek_next() < gen2.peek_next():
                ans.append(gen1.get_next())
            else:
                ans.append(gen2.get_next())
        
        while gen1.has_next():
            ans.append(gen1.get_next())
        
        while gen2.has_next():
            ans.append(gen2.get_next())
        
        return ans
        
    
    def dfs(self,node):
        if node.left:
            yield from self.dfs(node.left)
        if node:
            yield node.data
        if node.right:
            yield from self.dfs(node.right)

#{ 
 # Driver Code Starts.
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def buildTree(s):
    # Corner Case
    if len(s) == 0 or s[0] == 'N':
        return None
    
    # Creating list of strings from input string after splitting by space
    ip = s.split()
    
    # Create the root of the tree
    root = Node(int(ip[0]))
    
    # Push the root to the queue
    queue = [root]
    
    # Starting from the second element
    i = 1
    while queue and i < len(ip):
        # Get and remove the front of the queue
        currNode = queue.pop(0)
        
        # Get the current node's value from the string
        currVal = ip[i]
        
        # If the left child is not null
        if currVal != "N":
            # Create the left child for the current node
            currNode.left = Node(int(currVal))
            
            # Push it to the queue
            queue.append(currNode.left)
        
        # For the right child
        i += 1
        if i >= len(ip):
            break
        currVal = ip[i]
        
        # If the right child is not null
        if currVal != "N":
            # Create the right child for the current node
            currNode.right = Node(int(currVal))
            
            # Push it to the queue
            queue.append(currNode.right)
        i += 1
    
    return root



def main():
    t = int(input())
    for _ in range(t):
        s = input()
        root1 = buildTree(s)
        s = input()
        root2 = buildTree(s)
        obj = Solution()
        vec = obj.merge(root1, root2)
        print(" ".join(map(str, vec)))

if __name__ == "__main__":
    main()

# } Driver Code Ends