#User function Template for python3

class Solution:
    #Function to sort the array using bubble sort algorithm.
    def bubbleSort(self,arr, n):
        for i in range(len(arr)):
            for j in range(i+1,len(arr)):
                if arr[j]<arr[i]:
                    arr[i],arr[j]=arr[j],arr[i]
        return arr
                
        # code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3



if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ob.bubbleSort(arr, n)
        for i in arr:
            print(i,end=' ')
        print()

# } Driver Code Ends