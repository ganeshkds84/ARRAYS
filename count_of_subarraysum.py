class Ganesh():
    def count_of_subarrays(self,nums,k):
        count=0
        seen={0:1}
        c_sum=0
        for i in range(len(nums)):
            c_sum=c_sum+nums[i]
            if (c_sum-k) in seen:
                count+=seen[c_sum-k]
            seen[c_sum]=seen.get(c_sum,0)+1
        return count
    
Ashwika=Ganesh()
nums = [1, 2, 1, 2, 1]
k = 3
print(Ashwika.count_of_subarrays(nums,k))
