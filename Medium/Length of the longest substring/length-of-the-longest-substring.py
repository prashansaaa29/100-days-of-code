#User function Template for python3

class Solution:
    def longestUniqueSubsttr(self,S):
        a=set()
        l=0
        res=0
        for r in range(len(S)):
            while S[r]  in a:
                a.remove(S[l])
                l=l+1
            a.add(S[r])
            res=max(res,r-l+1)
        return res


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        s = input().strip()
        
        
        ob=Solution()
        print(ob.longestUniqueSubsttr(s))
# } Driver Code Ends