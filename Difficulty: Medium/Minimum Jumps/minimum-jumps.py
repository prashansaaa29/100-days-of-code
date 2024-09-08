#User function Template for python3
class Solution:
	def minJumps(self, arr):
	    n=len(arr)
        x=y=jumps=0
        for i in range(n-1):
            y=max(y, i+arr[i])
            if x==i:
               if y==i:
                   return -1
               jumps += 1
               x=y
        return jumps
	    #code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        # n = int(input())
        Arr = [int(x) for x in input().split()]
        ob = Solution()
        ans = ob.minJumps(Arr)
        print(ans)

# } Driver Code Ends