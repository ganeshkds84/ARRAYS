class Solution():
    def rotate_byk(self,nums,k):
        nums=nums+nums[:k+1]
        print(nums)
        nums=nums[k:]
        
        
        return nums
    
    
    
answer=Solution()
print(answer.rotate_byk([1,2,3,4,5],2))