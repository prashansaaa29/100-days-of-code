#User function Template for python3

class Solution:
    def Maximize(self, a):
        n=len(a)
        a.sort()
        sum=0
        for i in range(n):
            sum=sum+(a[i]*i)
        return sum%1000000007
        # Complete the function
      



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())

    for _ in range(t):
        A = list(map(int, input().strip().split()))
        # k = int(input())
        ob = Solution()
        print(ob.Maximize(A))

# } Driver Code Ends