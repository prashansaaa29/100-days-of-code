#User function Template for python3


class Solution:
    def compareFrac (self, str):
        '''a=str.split(',')
        maxi=0
        for i in a:
            b=i.split('/')
            c=int(b[0])/int(b[1])
            maxi=max(maxi,c)
        return maxi'''
        questions = [i.strip() for i in str.split(",")]
        lst = [eval(i) for i in questions]
        if lst[-1] == lst[-2]:
            return "equal"
        return questions[lst.index(max(lst))].strip()
        
        # code here
        



#{ 
 # Driver Code Starts
#Initial Template for Python 3
import re

if __name__ == '__main__':
    ob = Solution()
    t = int(input())
    for _ in range(t):
        str = input()
        print(ob.compareFrac(str))

# } Driver Code Ends