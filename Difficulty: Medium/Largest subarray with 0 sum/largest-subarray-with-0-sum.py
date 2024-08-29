from collections import defaultdict

class Solution:
    def maxLen(self, n, arr):
        dic = defaultdict(list)
        dic[0] = [-1]  # Initialize with -1 to handle the case when the zero-sum subarray starts from the beginning
        sumi = 0
        for i, j in enumerate(arr):
            sumi += j
            dic[sumi].append(i)
        maxilen = 0
        for indices in dic.values():
            if len(indices) > 1:
                maxilen = max(maxilen, max(indices) - min(indices))
        return maxilen

#{ 
 # Driver Code Starts
if __name__=='__main__':
    t= int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.maxLen(n ,arr))
# Contributed by: Harshit Sidhwa
# } Driver Code Ends