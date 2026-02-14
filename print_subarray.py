class Solution():
    def maxm_subarray(self,nums):
        c_sum=nums[0]
        m_sum=nums[0]
        f=0
        l=0
        for i in range(1,len(nums)):
            c_sum=c_sum+nums[i]
 
            if nums[i]>c_sum and nums[i]>m_sum:
                m_sum=nums[i]
                c_sum=nums[i]
                f=i
            elif c_sum>m_sum:
                m_sum=c_sum
                l=i
            elif nums[i]>c_sum:
                c_sum=nums[i]
                    
        return nums[f:l+1]
    
answer=Solution()
print(answer.maxm_subarray( [2, -1, 2, 3, 4, -5]))