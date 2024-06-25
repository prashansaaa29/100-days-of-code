class Solution:
    def rotateMatrix(self, k, mat):
        n=len(mat) # to get row
        m=len(mat[0]) # to get column

        # defining mat2, initializing every element with zero.
        mat2=[[0 for _ in range(m)] for _ in range(n)]
        k=k%m # if k is beyond column length 
        for i in range(n):
            for j in range(m):
                mat2[i][(m-k+j)%m]=mat[i][j]
        
        return mat2
        
        # code here



#{ 
 # Driver Code Starts
import math

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, m, k = map(int, input().strip().split(" "))
        mat = []
        for i in range(n):
            mat.append(list(map(int, input().strip().split(" "))))
        ob = Solution()
        ans = ob.rotateMatrix(k, mat)
        for i in range(n):
            for j in range(m):
                print(ans[i][j], end=" ")
            print()

# } Driver Code Ends