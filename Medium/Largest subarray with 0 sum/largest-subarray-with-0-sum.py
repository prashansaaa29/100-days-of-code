#Your task is to complete this function
#Your should return the required output
class Solution:
    def maxLen(self, n, arr):
        for i in range(1,n):
            arr[i] +=arr[i-1]
        res = 0
        dc = dict()
        for i, sm in enumerate(arr):
            if sm == 0:
                res = max(res, i+1)
            elif sm in dc:
                res = max(res, i-dc[sm])
            else:
                dc[sm] = i
        return res
             
        #Code here


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