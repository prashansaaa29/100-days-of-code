#User function Template for python3

class Solution:
    def transpose(self, matrix, n):
        arr = [[0]*n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                arr[i][j]=matrix[j][i]
        for i in range(n):
            for j in range(n):
                matrix[i][j]=arr[i][j]
        # Write Your code here


#{ 
 # Driver Code Starts

#Initial Template for Python 3

for _ in range(int(input())):
    n = int(input())
    matrix = [
            list(map(int,input().split()))
            for _ in range(n)
        ]
        
    ob = Solution()
    ob.transpose(matrix, n)
    
    for row in matrix:
        print(*row)
    
# } Driver Code Ends