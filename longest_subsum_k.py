class Solution():
    def longest_subsum(self, nums, k):
        left = 0
        current_sum = 0
        max_len = 0
        
        for right in range(len(nums)):
            current_sum += nums[right]
            
            while current_sum > k:
                current_sum -= nums[left]
                left += 1
            
            if current_sum == k:
                max_len = max(max_len, right - left + 1)
        
        return max_len
    
answer=Solution()
a=[1,2,3,1,1,1,1,4,2,3]
print(answer.longest_subsum(a,7))