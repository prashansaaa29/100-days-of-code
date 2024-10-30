from collections import defaultdict
class Solution:
    def countPairsWithDiffK(self,arr, k):
    # code here
        mp = defaultdict(int)
        res = 0
        for i in range(len(arr)):
            if abs(arr[i]-k) in mp :
                res += mp[arr[i]-k]
            if (arr[i]+k) in mp:
                res += mp[arr[i]+k]
            mp[arr[i]] +=1
            
        return res




#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        k = int(input().strip())
        ob = Solution()
        ans = ob.countPairsWithDiffK(arr, k)
        print(ans)
        print("~")
        tc -= 1

# } Driver Code Ends