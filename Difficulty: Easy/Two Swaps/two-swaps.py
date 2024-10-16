class Solution:
    def checkSorted(self, a):
        mismatch = 0
        swap_count = 0
        
        for i in range(len(a)):
            if arr[i] !=  i+1:
                mismatch +=1
        if mismatch == 1 or mismatch == 2 or mismatch > 4:
            return False
        if mismatch == 3 or mismatch == 0:
            return True
            
        # if mismatch is 4
        for i in range(len(a)):
            if a[i] != i+1:
                corr_index = a.index(i+1)
                a[a.index(i+1)] = a[i]
                a[i] = i+1
                swap_count+=1
                if swap_count > 2:
                    return False
        for i in range(len(a)):
            if a[i] != i+1:
                return False
        return True
        #code here


#{ 
 # Driver Code Starts
if __name__ == "__main__":
    t = int(input().strip())

    for _ in range(t):
        arr = list(map(int, input().split()))

        sol = Solution()
        result = sol.checkSorted(arr)
        if result:
            print("true")
        else:
            print("false")

# } Driver Code Ends