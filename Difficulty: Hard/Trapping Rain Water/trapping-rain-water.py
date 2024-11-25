
class Solution:
    def trappingWater(self, arr):
        maxleft=[0]*len(arr)
        maxright=[0]*len(arr)
        for x in range(1,len(arr)):
            maxleft[x]=max(maxleft[x-1],arr[x-1])
        for x in range(len(arr)-2,-1,-1):
            maxright[x]=max(maxright[x+1],arr[x+1])
        res=0
        for x in range(len(arr)):
            waterlevel=min(maxright[x],maxleft[x])
            if waterlevel>=arr[x]:
                res=res+(waterlevel-arr[x])
        return res
        
        
        
        
        
        
        
        
        # code here


#{ 
 # Driver Code Starts
#Initial template for Python 3

import math


def main():
    t = int(input())
    while (t > 0):

        arr = [int(x) for x in input().strip().split()]
        obj = Solution()
        print(obj.trappingWater(arr))

        t -= 1
        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends