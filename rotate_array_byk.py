class Solution():
    def rotate_byk(self,nums,k):
        k=k%len(nums)
        f=0
        l=k-1
        while f<l:
            nums[f],nums[l]=nums[l],nums[f]
            f+=1
            l-=1
        f=k
        l=len(nums)-1
        while f<l:
            nums[f],nums[l]=nums[l],nums[f]
            f+=1
            l-=1
        f=0
        l=len(nums)-1
        while f<l:
            nums[f],nums[l]=nums[l],nums[f]
            f+=1
            l-=1
        return nums    
    
answer=Solution()
print(answer.rotate_byk([1,2,3,4,5,6,7,8],3))