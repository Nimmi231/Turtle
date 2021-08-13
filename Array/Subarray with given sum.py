#User function Template for python3

#Function to find a continuous sub-array which adds up to a given number.
class Solution:
    def subArraySum(self,arr, n, s): 
        n = len(arr)
        left, right = 0, 0
        currSum = 0
        while currSum != s:
            if(currSum < s and right < n):
                currSum += arr[right]
                right += 1
            elif(currSum > s and left < n):
                currSum -= arr[left]
                left += 1
            else:
                return [-1]
        return [left+1, right]
        #Your code here

#{ 
#  Driver Code Starts
#Initial Template for Python 3

import math

def main():
        T=int(input())
        while(T>0):
            
            NS=input().strip().split()
            N=int(NS[0])
            S=int(NS[1])
            
            A=list(map(int,input().split()))
            ob=Solution()
            ans=ob.subArraySum(A, N, S)
            
            for i in ans:
                print(i, end=" ")
                
            print()
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends
