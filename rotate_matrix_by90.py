class Solution():
    def rotate_matrix(self,nums):
        for i in range(len(nums)):
            for j in range(i,len(nums)):
                nums[i][j],nums[j][i]=nums[j][i],nums[i][j]
        for k in range(len(nums)):
            i,j=0,len(nums)-1
            while i<j:
                nums[k][i],nums[k][j]=nums[k][j],nums[k][i]
                i+=1
                j-=1
                
        return nums
    
a=[
 [5,1,9,11],
 [2,4,8,10],
 [13,3,6,7],
 [15,14,12,16]
]
answer=Solution()
print(answer.rotate_matrix(a))
