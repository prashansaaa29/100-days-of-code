#User function Template for python3
import bisect
class Solution:
    
    #Function to find length of longest increasing subsequence.
    def longestSubsequence(self, n, arr):
        temp = [arr[0]]
        length = 1
        for i in range(1, n):
            if arr[i] > temp[-1]:
                temp.append(arr[i])
                length += 1
            else:
                ind = bisect.bisect_left(temp, arr[i])
                temp[ind] = arr[i]
        return length  
                
        
                
            
        # code here
       



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    for _ in range(int(input())):
        n = int(input())
        a = [int(x) for x in input().split()]
        ob = Solution()
        print(ob.longestSubsequence(n, a))

# } Driver Code Ends