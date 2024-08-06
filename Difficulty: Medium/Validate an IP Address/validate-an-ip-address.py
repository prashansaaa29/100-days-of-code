#User function Template for python3
class Solution:
    def isValid(self, s):
        for i in range(len(s)):

            #checking illegal character
            if s[i] != '.' and not(s[i] >= '0' and s[i] <= '9'):
                return 0
            s = s.split('.')
            if len(s) != 4:
                return 0
            for i in range(4):
                if len(s[i]) < 1 or len(s[i]) > 3:
                    return False
                if int(s[i]) < 0 or int(s[i]) > 255:
                    return 0
                if len(s[i]) >= 2 and s[i][0] == '0':
                    return 0
            return 1
        #code here



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    for _ in range(0, t):
        s = input()
        ob = Solution()
        if (ob.isValid(s)):
            print("true")
        else:
            print("false")

# } Driver Code Ends