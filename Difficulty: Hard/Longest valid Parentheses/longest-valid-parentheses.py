# User function Template for Python3

class Solution:
    def maxLength(self, str):
        curr_open = 0
        good_start_i = [-1]
        max_len = 0
        for i, c in enumerate(str):
            if c == "(":
                curr_open += 1
                good_start_i.append(i)
            else:  # ")"
                if curr_open > 0:
                    curr_open -= 1
                    good_start_i.pop()
                    max_len = max(max_len, i - good_start_i[-1])
                else:
                    good_start_i.clear()
                    good_start_i.append(i)
        return max_len
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