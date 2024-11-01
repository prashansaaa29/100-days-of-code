#User function Template for python3

class Solution:
    def maxSum(self,arr):
        n,ans=len(arr),0
        arr.sort()
        for i in range(n//2):
            ans-=(2*arr[i])
            ans+=(2*arr[n-1-i])
        return ans
        # code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))
        ob = Solution()
        ans = ob.maxSum(arr)  # Call maxSum method and store result in ans
        print(ans)  # Print the result
        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends