#User function Template for python3

class Solution:
    def rearrange(self,arr):
        i, j, n = 0, 0, len(arr)
        ret = []
        
        while i < n or j < n:
            while i < n and arr[i] < 0:
                i += 1
            while j < n and arr[j] >= 0:
                j += 1
            if i < n:
                ret.append(arr[i])
                i += 1
            if j < n:
                ret.append(arr[j])
                j += 1
        arr[:] = ret
        # code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ob.rearrange(arr)
        for x in arr:
            print(x, end=" ")
        print()
        tc -= 1

# } Driver Code Ends