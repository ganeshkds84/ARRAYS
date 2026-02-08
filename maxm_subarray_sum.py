class Answer():
    def maximum_csum(self,nums):
        csum=nums[0]
        msum=nums[0]
        for i in range(1,len(nums)):
            csum=csum+nums[i]
            if nums[i]>csum:
                msum=nums[i]
                csum=nums[i]
            elif csum>msum:
                msum=csum
        
        return msum
    
#a=list(map(int,input("Enter the numbers:").split()))
find=Answer()
print(find.maximum_csum([-2,1,-3,4,-1,2,1,-5,4]))