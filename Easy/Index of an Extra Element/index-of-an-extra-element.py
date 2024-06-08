class Solution:
    def findExtra(self,n,a,b):
        A=set(a)
        B=set(b)
        c=A-B
        return a.index(c.pop())


#{ 
 # Driver Code Starts
if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))
        print(Solution().findExtra(n, a, b))

# } Driver Code Ends