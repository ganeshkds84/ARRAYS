class Solution():
    def move_end(self,nums):
        if len(nums)<=1:
            return nums
        i,j=0,0
        for j in range(len(nums)):
            if nums[j]!=0:
                nums[i]=nums[j]
                i+=1
        while i<len(nums):
            nums[i]=0
            i+=1
                   
        return nums
        

answer=Solution()
a=[0,1,0,3,12]
print(answer.move_end(a))
