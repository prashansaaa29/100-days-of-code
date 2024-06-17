#User function template for Python

class Solution:
    def rectanglesInCircle(self,r):
        if r < 1 or r > 1000:
            return 0  # Return 0 if r is outside the valid range

        count = 0
        for length in range(1, 2 * r + 1):
            for width in range(1, 2 * r + 1):
                
                if length * length + width * width <= 4 * r * r:
                    count += 1

        return count


        #code here


#{ 
 # Driver Code Starts
#Initial Template for Python

import math

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        ans = ob.rectanglesInCircle(N)
        print(ans)

# } Driver Code Ends