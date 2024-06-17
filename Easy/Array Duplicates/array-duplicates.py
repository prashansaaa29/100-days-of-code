class Solution:
    def duplicates(self, arr, n): 
        temp = {}
        for val in arr:
            temp[val] = temp.get(val,0) + 1
        res = []
        for values in temp.items():
            if values[1] >1:
                res.append(values[0])
        if len(res) == 0:
            return [-1]
        else:
            res = sorted(res)
            return res
    	# code here
    	    


#{ 
 # Driver Code Starts
if(__name__=='__main__'):
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        res = Solution().duplicates(arr, n)
        for i in res:
            print(i,end=" ")
        print()



# } Driver Code Ends