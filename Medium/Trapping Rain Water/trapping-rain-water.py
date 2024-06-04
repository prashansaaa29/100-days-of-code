
class Solution:
    def trappingWater(self, arr,n):
        max_left=[0]*len(arr)
        for x in range(1,len(arr)):
            max_left[x]=max(arr[x-1],max_left[x-1])
        max_right=[0]*len(arr)
        for x in range(len(arr)-2,-1,-1):
            max_right[x]=max(arr[x+1],max_right[x+1])
        res=0
        for x in range(len(arr)):
            waterlevel=min(max_left[x],max_right[x])
            if waterlevel>=arr[x]:
                res=res+(waterlevel-arr[x])
        return res
            
        
        
            
        #Code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math



def main():
        T=int(input())
        while(T>0):
            
            n=int(input())
            
            arr=[int(x) for x in input().strip().split()]
            obj = Solution()
            print(obj.trappingWater(arr,n))
            
            
            T-=1


if __name__ == "__main__":
    main()



# } Driver Code Ends