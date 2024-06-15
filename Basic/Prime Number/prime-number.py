#User function Template for python3

class Solution:
    def isPrime (self, n):
         # checking for one it's not prime 
        # 1 is not prime number
        if(n<=1):
            return 0 
        # check 2,3 are prime numbers 
        if(n<=3):
            return 1
        #check number is even
        if(n%2==0):
            return 0 
        
        # check for odd nmubers starting 5 
        for i in range(3, int(n**0.5)+1, 2):
            if n%i == 0:
                return 0 
        return 1
                
        # code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
       

        ob = Solution()
        print(ob.isPrime(N))
# } Driver Code Ends