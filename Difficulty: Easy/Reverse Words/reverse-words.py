# User function Template for python3

class Solution:
    
    #Function to reverse words in a given string.
    def reverseWords(self,str):
        a=str.split('.')
        b=''
        for i in range(len(a)-1,-1,-1):
            b=b+a[i]+'.'
        return b[:len(b)-1]
        # code here 


#{ 
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        s = str(input())
        obj = Solution()
        print(obj.reverseWords(s))

# } Driver Code Ends