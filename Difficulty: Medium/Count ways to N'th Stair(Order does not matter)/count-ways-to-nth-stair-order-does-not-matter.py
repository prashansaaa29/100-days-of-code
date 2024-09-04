#User function Template for python3

class Solution:
	def nthStair(self,n):
	    if n == 1 or n == 2: return n
        
        dp = [0] * (n+1)
        
        dp[1],dp[2] = 1,2
        
        for idx in range(3,n+1):
            
            dp[idx] = dp[idx-1]+1 if idx % 2 == 0 else dp[idx-1]
            
        return dp[n]
		# Code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys
sys.setrecursionlimit(10**6)

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		ob = Solution();
		ans = ob.nthStair(n)
		print(ans)
# } Driver Code Ends