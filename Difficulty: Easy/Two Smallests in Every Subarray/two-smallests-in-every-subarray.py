class Solution:
    def pairWithMaxSum(self, arr):
        a = len(arr)
        
        if a < 2:
            return -1
        
        ans = arr[0] + arr[1]
        for i in range(1, a - 1):
            ans = max(ans, arr[i] + arr[i + 1])
        
        return ans
        #code here


#{ 
 # Driver Code Starts
if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().strip().split("\n")

    t = int(data[0])
    lines = data[1:]

    for line in lines:
        s = list(map(int, line.strip().split()))
        solution = Solution()
        res = solution.pairWithMaxSum(s)
        print(res)

# } Driver Code Ends