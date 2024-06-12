#User function Template for python3
class Solution:
     
    #Function to find if there exists a triplet in the 
    #array A[] which sums up to X.
    def find3Numbers(self,A, n, X):
        '''    A.sort()
        for i in range(n-2):
            left=i+1
            right=n-1
            while left<right:
                curr=A[i]+A[left]+A[right]
                if curr==X:
                    return 1
                elif curr>X:
                    right-=1
                elif curr<X:
                    left+=left
        return 0'''
        A.sort()
        
        # Iterate through the array
        for i in range(n - 2):
            # Use two pointers to find the remaining two numbers
            left = i + 1
            right = n - 1
            
            while left < right:
                current_sum = A[i] + A[left] + A[right]
                
                if current_sum == X:
                    return 1
                elif current_sum < X:
                    left += 1
                else:
                    right -= 1
        
        return 0
        
            
        # Your Code Here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n,X=map(int,input().strip().split())
        A=list(map(int,input().strip().split()))
        ob=Solution()
        if(ob.find3Numbers(A,n,X)):
            print(1)
        else:
            print(0)
# } Driver Code Ends