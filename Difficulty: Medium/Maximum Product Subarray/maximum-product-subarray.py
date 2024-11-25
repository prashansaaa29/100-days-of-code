#User function Template for python3
class Solution:

	# Function to find maximum
	# product subarray
	def maxProduct(self,arr):
	     # Initialize the maximum, minimum, and result to the first element

        max_product = min_product = result = arr[0]

 

        # Iterate over the array starting from the second element

        for i in range(1, len(arr)):

            # If the current element is negative, swap max_product and min_product

            if arr[i] < 0:

                max_product, min_product = min_product, max_product

            

            # Update max_product and min_product

            max_product = max(arr[i], max_product * arr[i])

            min_product = min(arr[i], min_product * arr[i])

 

            # Update the result with the maximum value found so far

            result = max(result, max_product)

 

        return result
	    
		# code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.maxProduct(arr)
        print(ans)
        tc -= 1

# } Driver Code Ends