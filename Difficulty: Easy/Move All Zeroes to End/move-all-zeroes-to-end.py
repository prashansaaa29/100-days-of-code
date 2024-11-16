#User function Template for python3

class Solution:
	def pushZerosToEnd(self,arr):
	    tmp_arr = []
        count_zero = 0
        for i in range(len(arr)):
        	if(arr[i]==0):
        		count_zero += 1
        	else:
        		tmp_arr.append(arr[i])
        res_arr = tmp_arr + [0]*count_zero
        for i in range(len(res_arr)):
            arr[i] = res_arr[i]
    	# code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ob.pushZerosToEnd(arr)
        for x in arr:
            print(x, end=" ")
        print()
        tc -= 1
# } Driver Code Ends