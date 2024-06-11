
class Solution:
    def countNumberswith4(self, n : int) -> int:
        count=0
        for i in range(4,n+1):
            a=str(i)
            if '4' in a:
                count=count+1
        return count
            
        
        # code here
        



#{ 
 # Driver Code Starts
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):

        n = int(input())

        obj = Solution()
        res = obj.countNumberswith4(n)

        print(res)

# } Driver Code Ends