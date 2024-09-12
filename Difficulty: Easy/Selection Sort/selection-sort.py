#User function Template for python3

class Solution: 
    def select(self, arr, i):
        min_v=i
        for j in range(i+1,len(arr)):
                if arr[j]<arr[min_v]:
                    min_v=j
                    
        return min_v
        # code here 
    
    def selectionSort(self, arr,n):
        for i in range(len(arr)-1):
            min_value=self.select(arr,i)
            arr[i],arr[min_value]=arr[min_value],arr[i]
    
            
            
                    
                    
            
        #code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        Solution().selectionSort(arr, n)
        for i in range(n):
            print(arr[i],end=" ")
        print()
# } Driver Code Ends