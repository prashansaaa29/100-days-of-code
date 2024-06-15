#User function Template for python3

#User function Template for python3
class Solution:

	def nthRowOfPascalTriangle(self,n):
	    if n==0:
	        return None
	    m=(10**9)+7
	    p=[0]*n
	    p[0]=1
	    for i in range(1,n):
	        for j in range(i,0,-1):
                p[j] = (p[j] + p[j - 1]) % m
                #print(p)
        return p
	            
	    
	    # code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 

	tc=int(input())
	while tc > 0:
	    n=int(input())
	    ob = Solution()
	    ans=ob.nthRowOfPascalTriangle(n)
	    for x in ans:
	        print(x, end=" ")
	    print()
	    tc=tc-1
# } Driver Code Ends