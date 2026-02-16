class Solution():
    def rearrange_array(self,nums):
        i,j=0,0
        positive=[]
        negative=[]
        final=[]
        for i in range(len(nums)):
            if nums[i]>0:
                positive.append(nums[i])
            else:
                negative.append(nums[i])
        
        for i in range(len(positive)):
            final.append(positive[i])
            final.append(negative[i])
        
        return final
    
answer=Solution()
print(answer.rearrange_array([-9,-8,-5,3,1,-2,-6,6,7,8,2,-4]))