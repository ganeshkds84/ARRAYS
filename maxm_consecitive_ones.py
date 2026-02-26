class Solution():
    def consecutive_ones(self,nums):
        count=0
        temp=0
        for i in range(len(nums)):
            if nums[i]==1:
                temp+=1
                if temp>count:
                    count=temp
            else:
                temp=0
        
        return count    
    
answer=Solution()
a=[1,0,1,1,0,1]
print(answer.consecutive_ones(a))