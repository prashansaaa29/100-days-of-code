
from typing import List


class Solution:
    def getPrimes(self, n : int) -> List[int]:
        primes = [True]*(n+1)
        primes[0] = False
        primes[1] = False
        
        for i in range(n+1):
            if not primes[i]:
                continue
            for k in range(i*i, n+1, i):
                primes[k] = False
                
        #print(primes)
        for k in range(n+1):
            if primes[k] and primes[n-k]:
                return k, n-k
        
        return -1, -1
        



#{ 
 # Driver Code Starts
class IntArray:

    def __init__(self) -> None:
        pass

    def Input(self, n):
        arr = [int(i) for i in input().strip().split()]  #array input
        return arr

    def Print(self, arr):
        for i in arr:
            print(i, end=" ")
        print()


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):

        n = int(input())

        obj = Solution()
        res = obj.getPrimes(n)

        IntArray().Print(res)

# } Driver Code Ends