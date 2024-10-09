class Solution:
    
    #Function is to check whether two strings are anagram of each other or not.
    def isAnagram(self, str1, str2):
        s1 = sorted(str1)
        s2 = sorted(str2)
        if s1 == s2:
            return 1
        return 0
        #code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        a, b = map(str, input().strip().split())
        if (Solution().isAnagram(a, b)):
            print("YES")
        else:
            print("NO")

# } Driver Code Ends