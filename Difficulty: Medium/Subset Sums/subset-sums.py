#User function Template for python3
class Solution:
	def subsetSums(self, arr, n):
	    ans=[]
	    def subset(i,arr,s):
	        if i==len(arr):
	            ans.append(s)
	            return 
	        subset(i+1,arr,s+arr[i])
	        subset(i+1,arr,s)
	    subset(0,arr,0)
	    ans.sort()
	    return ans
	        
	        
	        
	        
	        
	        
	        
	    
	    
	    
	        
	    
		# code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        N = int(input())
        arr = [int(x) for x in input().split()]
        ob = Solution()
        ans = ob.subsetSums(arr, N)
        ans.sort()
        for x in ans:
            print(x, end=" ")
        print("")

# } Driver Code Ends