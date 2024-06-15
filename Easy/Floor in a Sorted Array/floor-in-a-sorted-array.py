class Solution:
    #User function Template for python3
    
    #Complete this function
    def findFloor(self,A,N,X):
        l=[]
        for i in A:
            if i<=X:
                l.append(i)
        if len(l)==0:
            return -1
        else:
            return A.index(l[-1])
        #Your code here
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3


import math


def main():
        T=int(input())
        while(T>0):
            
            NX=[int(x) for x in input().strip().split()]
            N=NX[0]
            X=NX[1]

            A=[int(x) for x in input().strip().split()]
            
            obj = Solution()
            print(obj.findFloor(A,N,X))
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends