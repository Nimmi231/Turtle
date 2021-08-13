#User function template for Python 3

class Solution:
    def majorityElement(self, A, N):
        bag = {}
        for i in A:
            if i not in bag:
                bag[i]=1
            else:
                bag[i]+=1
        for key,value in bag.items():
            if value>N//2:
                return key
        return -1
        
        
       
        





        
 
 
            
        #Your code here

#{ 
#  Driver Code Starts
#Initial Template for Python 3

import math

from sys import stdin


def main():
        T=int(input())
        while(T>0):
            
            N=int(input())

            A=[int(x) for x in input().strip().split()]
            
            
            obj = Solution()
            print(obj.majorityElement(A,N))
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends
