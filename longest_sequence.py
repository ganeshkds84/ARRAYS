class Solution():
    def longest_sequence(self, nums):
        if not nums:
            return 0
        
        nums = sorted(nums)
        
        count = 1
        longest = 1
        
        for i in range(1, len(nums)):
            
            if nums[i] == nums[i-1]:
                continue
                
            elif nums[i] == nums[i-1] + 1:
                count += 1
            else:
                longest = max(longest, count)
                count = 1
        
        longest = max(longest, count)
        return longest


answer = Solution()
print(answer.longest_sequence([1,2,2,3]))
