#User function Template for python3

class Solution:
    def findTwoElement( self,arr):
        n = len(arr)   # length of arr
        sum_exp = int(n * (n + 1) / 2)   # expected sum
        sum_arr = sum(arr)   # actual sum
        
        set_arr = set(arr)   # unqique elements in arr
        sum_set = sum(set_arr)   # sum of the unique elements
        
        repeating = sum_arr - sum_set
        missing = sum_exp - sum_set
        
        return([repeating, missing])
        # code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.findTwoElement(arr)
        print(str(ans[0]) + " " + str(ans[1]))
        tc = tc - 1

# } Driver Code Ends