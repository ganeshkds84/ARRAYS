class Solution():
    def rotate_array(self,nums):
        temp=nums[0]
        for i in range(len(nums)-1):
            nums[i]=nums[i+1]
        nums[len(nums)-1]=temp
        
        return nums
    
a=list(map(int,input("Enter numbers:").split()))
answer=Solution()
print(answer.rotate_array(a))