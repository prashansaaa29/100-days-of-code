#User function Template for python3

class Solution:
    
    #Function to return max value that can be put in knapsack of capacity W.
    def knapSack(self,W, wt, val):
        n=len(wt)
        dp=[[0 for i in range(W+1)] for j in range(n+1)]
        for i in range(1,n+1):
            for w in range(1,W+1):
                if w-wt[i-1]>=0:
                    dp[i][w]=max(dp[i-1][w],dp[i-1][w-wt[i-1]]+val[i-1])
                else:
                    dp[i][w]=dp[i-1][w]
        return dp[n][W]
                
        
                


       
        # code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        # n = int(input())
        W = int(input())
        val = list(map(int, input().strip().split()))
        wt = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.knapSack(W, wt, val))

# } Driver Code Ends