def longest_subarray(nums,k):
    length,final=0,0
    for i in range(len(nums)):
        c_sum=0
        #c_sum=nums[i]
        for j in range(i,len(nums)):
            c_sum=c_sum+nums[j]
            if c_sum==k:
                length=j-i+1
                final=max(length,final)
    
    return final            
    


nums = [1,4,-5,4,6,5,-3,-3,-7,4]
K = 3
print(longest_subarray(nums,K))
            