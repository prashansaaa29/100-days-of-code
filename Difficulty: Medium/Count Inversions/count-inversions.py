class Solution:
    #User function Template for python3
    
    # arr[]: Input Array
    # N : Size of the Array arr[]
    #Function to count inversions in the array.
    def inversionCount(self, arr, n):
        def merge_and_count(arr, temp_arr, left, mid, right):
            i = left    # Starting index for left subarray
            j = mid + 1 # Starting index for right subarray
            k = left    # Starting index to be sorted
            inv_count = 0

            # Conditions are checked to ensure that i doesn't exceed mid and j doesn't exceed right
            while i <= mid and j <= right:
                if arr[i] <= arr[j]:
                    temp_arr[k] = arr[i]
                    i += 1
                else:
                    # There are mid - i inversions because all the remaining elements in the left subarray
                    # (arr[i], arr[i+1], ..., arr[mid]) are greater than arr[j]
                    temp_arr[k] = arr[j]
                    inv_count += (mid - i + 1)
                    j += 1
                k += 1

            # Copy the remaining elements of left subarray, if any
            while i <= mid:
                temp_arr[k] = arr[i]
                i += 1
                k += 1

            # Copy the remaining elements of right subarray, if any
            while j <= right:
                temp_arr[k] = arr[j]
                j += 1
                k += 1

            # Copy the sorted subarray into Original array
            for i in range(left, right + 1):
                arr[i] = temp_arr[i]
                
            return inv_count

        # Helper function to use divide and conquer method to sort the array and count inversions
        def merge_sort_and_count(arr, temp_arr, left, right):
            inv_count = 0
            if left < right:
                mid = (left + right) // 2

                inv_count += merge_sort_and_count(arr, temp_arr, left, mid)
                inv_count += merge_sort_and_count(arr, temp_arr, mid + 1, right)
                inv_count += merge_and_count(arr, temp_arr, left, mid, right)

            return inv_count

        temp_arr = [0] * n
        return merge_sort_and_count(arr, temp_arr, 0, n - 1)
    
        '''
        def mergeSort(arr, l, r):
        m=len(arr)//2
        left=arr[l:m+1]
        right=arr[m+1:r+1]
        
        mergeSort(left,0,len(left))
        mergeSort(right,0,len(right))
        
        a=0
        b=0
        c=0
        while a<len(left) and b<len(right):
            if left[a]<right[c]:
                arr[b]=left[a]
                a=a+1
            elif left[a]>right[c]:
                arr[b]=right[c]
                c=c+1
            b=b+1
            
            
        while a<len(left):
            arr[b]=left[a]
            a=a+1
            b=b+1
        while c<len(right):
            arr[b]=left[c]
            c=c+1
            b=b+1'''
                    
            
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


if __name__ == '__main__':
    t = int(input())
    for tt in range(t):
        n = int(input())
        a = list(map(int, input().strip().split()))
        obj = Solution()
        print(obj.inversionCount(a, n))

# } Driver Code Ends