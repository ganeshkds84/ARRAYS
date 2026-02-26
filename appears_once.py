class Solution():
    def appears_once(self,nums):
        req=nums[0]
        for i in range(1,len(nums)):
            req=req^nums[i]
        
        return req
        
answer=Solution()
a=[1]
print(answer.appears_once(a))