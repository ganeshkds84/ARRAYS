class Ganesh():
    def array_inversion(self,nums):
        count=0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]>nums[j]:
                    count+=1
        
        return count

nums=[5,4,3,2,1]
Ashwika=Ganesh()
print(Ashwika.array_inversion(nums))