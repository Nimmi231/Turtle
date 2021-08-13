#User function Template for python3
class Solution:
    ##Complete this function
    #Function to rearrange  the array elements alternately.
    def rearrange(self,arr, n): 
        bag  =[]
        i = 0
        j = n-1
        
        for i in range(0,n):
            
            bag.append(arr[j])
            j-=1
            bag.append(arr[i])
            i+=1
        for i in range(n):
            arr[i]=bag[i]
            
        #print(bag)
        
            
            
        ##Your code here

#{ 
#  Driver Code Starts
#Initial Template for Python 3

import math




def main():
        T=int(input())
        while(T>0):
            
            n=int(input())
            
            arr=[int(x) for x in input().strip().split()]
            
            ob=Solution()
            ob.rearrange(arr,n)
            
            for i in arr:
                print(i,end=" ")
            
            print()
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends
