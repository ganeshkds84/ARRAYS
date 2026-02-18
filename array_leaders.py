class Solution():
    def array_leaders(self,nums):
        i=len(nums)-1
        final=[nums[i]]
        leader=nums[i]
        while i>0:
            if nums[i-1]>leader:
                leader=nums[i-1]
                final.append(leader)
                i-=1
            else:
                i-=1
                
        return final
    
    
answer=Solution()
print(answer.array_leaders([6,7,8,9]))