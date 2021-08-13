class Solution:
    def trappingWater(self, arr,n):
        size = len(arr)
        left = size * [0]
        right = size * [0]
        water = 0
        left[0]=arr[0]
        max_left = arr[0]
        for i in range(0,size):
            if(max_left < arr[i]):
                max_left = arr[i]
                left[i]=max_left
            else:
                left[i]=max_left
        max_right = arr[-1]
        for i in range(size-1,-1,-1):
            if(max_right < arr[i]):
                max_right = arr[i]
                right[i] = max_right
            else:
                 right[i] = max_right
        for i in range(0,size):
            water = water + min(left[i],right[i])-arr[i]
        return water
                
        
        #Code here

#{ 
#  Driver Code Starts
#Initial Template for Python 3

import math



def main():
        T=int(input())
        while(T>0):
            
            n=int(input())
            
            arr=[int(x) for x in input().strip().split()]
            obj = Solution()
            print(obj.trappingWater(arr,n))
            
            
            T-=1


if __name__ == "__main__":
    main()



# } Driver Code Ends
