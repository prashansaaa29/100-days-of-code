#User function Template for python3

#Complete this function
#Function to find maximum circular subarray sum.
def circularSubarraySum(arr):
    # Compute total sum of the array
    total_sum = sum(arr)

    # Helper function to calculate max or min subarray sum using Kadane's Algorithm
    def kadane(arr, find_max):
        running, result = 0, float('-inf') if find_max else float('inf')
        for e in arr:
            running = (max if find_max else min)(e, running + e)
            result = (max if find_max else min)(result, running)
        return result

    # Maximum subarray sum (non-circular)
    max_subarray_sum = kadane(arr, True)

    # Minimum subarray sum (to find the worst-case wrap-around sum)
    min_subarray_sum = kadane(arr, False)

    # If all elements are negative, return the maximum subarray sum (non-circular)
    if total_sum == min_subarray_sum:
        return max_subarray_sum

    # Maximum of non-circular and circular subarray sums
    return max(max_subarray_sum, total_sum - min_subarray_sum)
    ##Your code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math
import sys

if __name__ == "__main__":
    T = int(input())
    while (T > 0):

        arr = [int(x) for x in input().strip().split()]

        print(circularSubarraySum(arr))

        T -= 1

# } Driver Code Ends