class Goutham():
    def reverse_pairs(self,nums):
        count=0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]>2*nums[j]:
                    count+=1
                    
        return count
        
    
nums=list(map(int,input("Enter any numbers:").split(" ")))
Ashu=Goutham()
print(Ashu.reverse_pairs(nums))
