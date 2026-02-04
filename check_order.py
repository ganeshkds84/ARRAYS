class Solution:
    def is_sorted(self,nums):
        for i in range(1,len(nums)):
            if nums[i]<nums[i-1]:
                #print(nums[i],nums[i-1])
                return False
        return True
a=list(map(int,input("Enter numbers:").split()))
check=Solution()
print(check.is_sorted(a))