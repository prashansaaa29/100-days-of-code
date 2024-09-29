
class Solution:
    def trappingWater(self, arr):
        max_left=0
        max_right=0
        l=0
        r=len(arr)-1
        water=0
        if len(arr)<3:
            return(0)
        while l<r:
            max_left=max(max_left,arr[l])
            max_right=max(max_right,arr[r])
            if max_left<=max_right:
                water=water+(max_left-arr[l])
                l=l+1
            else:
                water=water+(max_right-arr[r])
                r=r-1
        return water
                
                
            
            
            
            
            
        #Code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math


def main():
    T = int(input())
    while (T > 0):

        n = int(input())

        arr = [int(x) for x in input().strip().split()]
        obj = Solution()
        print(obj.trappingWater(arr))

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends