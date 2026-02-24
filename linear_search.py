class Solution:
    def linearSearch(self, nums, target):
        for i in range(len(nums)):
            if nums[i] == target:
                return i
        return -1
    
nums = [1,2,3]
target = 3
answer=Solution()
print(answer.linearSearch(nums,target))