#User function Template for python3

class Solution:
    #Function to find triplets with zero sum.    
    def findTriplets(self, arr, n):
        '''for i in range(n):
            for j in range(i+1,n):
                a=arr[i]+arr[j]
                if -a in arr and arr.index(-a)!=i and arr.index(-a)!=j:
                    return 1
        return 0'''
        st=set()
        ln= len(arr)
        x=0
        st.add(arr[0])
        for i in range(1,ln-1):
            for j in range(i+1,ln):
                if x-arr[i]-arr[j] in st:
                    return True
            st.add(arr[i])
        return False


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
        n=int(input())
        a=list(map(int,input().strip().split()))
        if(Solution().findTriplets(a,n)):
            print(1)
        else:
            print(0)
# } Driver Code Ends