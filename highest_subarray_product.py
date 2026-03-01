class Solution():
    def highest_product(self,nums):
        final=nums[0]
        for i in range(len(nums)):
            product=1
            for j in range(i,len(nums)):
                product=product*nums[j]
                final=max(product,final)
        
        return final


answer=Solution()
nums=list(map(int,input("Enter any numbers:").split(" ")))
print(answer.highest_product(nums))