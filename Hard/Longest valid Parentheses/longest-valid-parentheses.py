# User function Template for Python3

class Solution:
    def maxLength(self, s):
        n = len(s)
        stack = []
        maxlength = [0]*(n+1)
        for currindex in range(n):
            if s[currindex] == '(':
                stack.append(currindex)
            else:
                if stack:
                    lastindex = stack.pop()
                    maxlength[currindex] = currindex-lastindex+1+maxlength[lastindex-1]
        return max(maxlength)
        
                
                
                
        # code here


#{ 
 # Driver Code Starts
# Initial Template for Python3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        S = input()
        
        ob = Solution()
        print(ob.maxLength(S))
# } Driver Code Ends