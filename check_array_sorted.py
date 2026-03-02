class Solution():
    def check(self,nums):
        n=len(nums)
        count=0
        for i in range(len(nums)):
            if nums[i]>nums[(i+1)%n]:
                count+=1
                #print(count)
                if count>1:
                    return False
            print(count)
        return True
    
nums=[3,4,5,1,2]
answer=Solution()
print(answer.check(nums))