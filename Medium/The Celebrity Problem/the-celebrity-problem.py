#User function Template for python3

class Solution:
    
    #Function to find if there is a celebrity in the party or not.
    def celebrity(self, M, n):
        left = 0
        right = n - 1

        while left < right:
            if M[left][right] == 1:
                left += 1
            else:
                right -= 1
    
        #Verify if left is a celebrity
        for i in range(n):
            if i != left and (M[i][left] == 0 or M[left][i] == 1):
                return -1
        return left if sum(M[left]) == 0 else -1
        # code here 



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t) :
        n = int(input())
        a = list(map(int,input().strip().split()))
        k = 0
        m = []
        for i in range(n):
            row = []
            for j in range(n):
                row.append(a[k])
                k+=1
            m.append(row)
        ob = Solution()
        print(ob.celebrity(m,n))
# } Driver Code Ends