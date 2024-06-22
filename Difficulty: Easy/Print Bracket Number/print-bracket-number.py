#User function Template for python3
class Solution:
	def bracketNumbers(self, str):
	    result = []
        count = 0
        stack = []
        for item in S:
            if item == '(':
                count += 1
                result.append(count)
                stack.append(count)
            if item == ')':
                result.append(stack.pop())
        return result
	             
		# code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        S = input()
        ob = Solution()
        answer = ob.bracketNumbers(S)
        for value in answer:
            print(value, end=" ")
        print()

# } Driver Code Ends