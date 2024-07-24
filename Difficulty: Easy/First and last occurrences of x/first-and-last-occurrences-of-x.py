#User function Template for python3
class Solution: 
    def firstAndLast(self, x, arr):
        if x not in arr:
            return [-1]
        else:
            a=arr.index(x)
            arr.sort(reverse=True)
            b=(len(arr)-1)-(arr.index(x))
            l=[a,b]
            return l
        # Code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        x = int(input())
        arr = [int(i) for i in input().split()]
        ob = Solution()
        ans = ob.firstAndLast(x, arr)
        s = (" ").join(map(str, ans))
        print(s)

# } Driver Code Ends