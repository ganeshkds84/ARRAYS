class Ganesh():
    def count_of_subarrays(self,nums,k):
        count=0
        for i in range(len(nums)):
            c_sum=0
            for j in range(i,len(nums)):
                c_sum=c_sum+nums[j]
                
                if c_sum==k:
                    count+=1
                    
        return count
    
Ashwika=Ganesh()
nums=[1,1,1,1,1]
k=3
print(Ashwika.count_of_subarrays(nums,k))
