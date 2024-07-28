#User function Template for python3
class Solution:

	def rowWithMax1s(self,arr):
	    m=0
	    for i in arr:
	        c=i.count(1)
	        m=max(m,c)
	    if m==0:
	        return -1
	    for j in arr:
	        if j.count(1)==m:
	            return arr.index(j)
		# code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, m = list(map(int, input().strip().split()))

        inputLine = list(map(int, input().strip().split()))
        arr = [[0 for j in range(m)] for i in range(n)]

        for i in range(n):
            for j in range(m):
                arr[i][j] = inputLine[i * m + j]
        ob = Solution()
        ans = ob.rowWithMax1s(arr)
        print(ans)
        tc -= 1

# } Driver Code Ends