class Solution:
    def findSplit(self, arr):
        total_sum = sum(arr)
        
        # If total sum is not divisible by 3, return -1, -1
        if total_sum % 3 != 0:
            return [-1, -1]
        
        target_sum = total_sum // 3
        current_sum = 0
        count = 0
        first_split_index = -1
        second_split_index = -1
        
        for i in range(len(arr)):
            current_sum += arr[i]
            
            # When we find the first part
            if current_sum == target_sum and count == 0:
                first_split_index = i
            
            # When we find the second part
            if current_sum == 2 * target_sum:
                count += 1
                second_split_index = i
            
            # If we found two parts, we can stop as we only need the indices
            if count == 1 and first_split_index != -1:
                break
        
        # Ensure there is at least a third part remaining
        if count == 1 and second_split_index < len(arr) - 1:
            return [first_split_index, second_split_index]
        
        return [-1, -1]



#{ 
 # Driver Code Starts
# Initial Template for Python 3

# Main
if __name__ == '__main__':
    t = int(input())
    while t:
        t -= 1
        arr = [int(x) for x in input().strip().split()]

        ob = Solution()
        result = ob.findSplit(arr)

        if (result == [-1, -1]) or len(result) != 2:
            print("false")
        else:
            sum1 = sum2 = sum3 = 0
            for i in range(len(arr)):
                if i <= result[0]:
                    sum1 += arr[i]
                elif i <= result[1]:
                    sum2 += arr[i]
                else:
                    sum3 += arr[i]

            if sum1 == sum2 == sum3:
                print("true")
            else:
                print("false")
        print("~")

# } Driver Code Ends