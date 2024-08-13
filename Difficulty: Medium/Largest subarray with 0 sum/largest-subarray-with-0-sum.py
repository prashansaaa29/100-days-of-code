#Your task is to complete this function
#Your should return the required output
class Solution:
    def maxLen(self, n, arr):
        '''sum_map = {}  # Dictionary to store (cumulative sum, index) pairs
        max_len = 0   # Variable to keep track of the maximum subarray length
        curr_sum = 0  # Variable to store the cumulative sum
        
        for i in range(n):
            curr_sum += arr[i]
            
            if curr_sum == 0:
                max_len = i + 1  # If cumulative sum is 0, the subarray from the start to the current index has a sum of zero
                
            if curr_sum in sum_map:
                max_len = max(max_len, i - sum_map[curr_sum])
            else:
                sum_map[curr_sum] = i  # Store the first occurrence of the cumulative sum
                
        return max_len'''
        a={}
        s=0
        t=0
        for i in range(n):
            s=s+arr[i]
            if s==0:
                t=i+1
            if s not in a:
                a[s]=i
            else:
                t=max(t,i-a[s])
        #print(a)
        return (t)
            
            
        #print(sum(arr))
        '''b=0
        i=n-1
        j=0
        while i>=j:
            s=sum(arr)
            #print(sum(arr))
            #print(arr)
            #print (i,j)
            if sum(arr)>0:
                if arr[i]>arr[j] and arr[i]>0:
                    arr.pop(i)
                    #i=i-1
                elif arr[j]>arr[i] and arr[j]>0:
                    arr.pop(j)
                
                    #j=j+1
            elif sum(arr)==0:
                return (len(arr))
                break
            else:
                if arr[j]<arr[i] and arr[j]<0:
                    arr.pop(j)
                elif arr[i]<arr[j] and arr[i]<0:
                    arr.pop(i)
                
            i=i-1'''
            #j=j+1
                
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