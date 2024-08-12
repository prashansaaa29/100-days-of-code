#User function Template for python3


#Complete this function
class Solution:
    def floorSqrt(self, n):
        lo, hi = 0, n+1
        while lo < hi:
            mi = lo+(hi-lo)//2
            if mi*mi > n:
                hi = mi
            else:
                lo = mi+1
        return lo-1
    #Your code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math


def main():
    T = int(input())
    while (T > 0):

        x = int(input())

        print(Solution().floorSqrt(x))

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends