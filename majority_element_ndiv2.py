class Solution():
    def majority_element(self,nums):
        major=None
        count=0
        for i in range(len(nums)):
            if count==0:
                    major=nums[i]
                    count=1
            elif nums[i]==major:
                count+=1
            
            else:
                count-=1
        
        return major
    
    
a=int(input("Enter the size of list:"))
b=list(map(int,input("Enter the numbers:").split()))
obj=Solution()
print(obj.majority_element(b))