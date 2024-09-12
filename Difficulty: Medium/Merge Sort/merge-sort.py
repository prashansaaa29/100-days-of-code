#User function Template for python3

class Solution:
    def merge(self,arr, l, m, r):
        left=arr[l:m+1]
        right=arr[m+1:r+1]
        i=0
        j=0
        k=l
        while i<len(left) and j<len(right):
            if left[i]<right[j]:
                arr[k]=left[i]
                i=i+1
            else:
                arr[k]=right[j]
                j=j+1
            k=k+1
        while i<len(left):
                arr[k]=left[i]
                i=i+1
                k=k+1
        while j<len(right):
                arr[k]=right[j]
                j=j+1
                k=k+1
        
    def mergeSort(self,arr, l, r):
        if l<r:
            mid=(l+r)//2
            self.mergeSort(arr,l,mid)
            self.mergeSort(arr,mid+1,r)
            self.merge(arr, l, mid, r)
        
            
            
        
        
        #code here



#{ 
 # Driver Code Starts
#Initial Template for Python 3


import sys
input = sys.stdin.readline
if __name__ == "__main__":
    t=int(input())
    for i in range(t):
        n=int(input())
        arr=list(map(int,input().split()))
        Solution().mergeSort(arr, 0, n-1)
        for i in range(n):
            print(arr[i],end=" ")
        print()
# } Driver Code Ends