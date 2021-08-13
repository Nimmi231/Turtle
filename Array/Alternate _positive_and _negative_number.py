class Solution:
    def rearrange(self,arr, n):
        a = []
        b = []
        for i in arr:
            if i>=0:
                a.append(i)
            else:
                b.append(i)
        j = 1
        for i in b:
            a.insert(j,i)
            j = j+2
        
        #print(a)
        #print(b)
        for i in range(n):
            arr[i] = a[i]
         #code here

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	tc = int(input())
	while tc > 0:
		n = int(input())
		arr = list(map(int, input().strip().split()))
		ob = Solution()
		ob.rearrange(arr, n)
		for x in arr:
			print(x, end=" ")
		print()
		tc -= 1

# } Driver Code Ends
