class Solution():
    def matrix_zero(self,nums,m,n):
        for i in range(m):
            for j in range(n):
                if nums[i][j]==0:
                    k,l=0,0
                    while k<m:
                        nums[k][j]=None
                        k+=1
                    while l<n:
                        nums[i][l]=None
                        l+=1
        for i in range(m):
            for j in range(n):
                if nums[i][j]==None:
                    nums[i][j]=0
                    
        return nums
    
answer=Solution()
a = [
 [1,5,1],
 [1,0,1],
 [1,1,1],
 [1,0,0]
]
print(answer.matrix_zero(a,4,3))