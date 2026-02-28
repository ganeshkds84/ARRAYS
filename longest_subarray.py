def longest_subarray(nums,k):
    length,final=0,0
    seen={}
    c_sum=0
    for i in range(len(nums)):
        c_sum=c_sum+nums[i]
        if c_sum==k:
            final=i+1
        if (c_sum-k) in seen:
            length=i-seen[c_sum-k]
            final=max(length,final)
        if (c_sum-k) not in seen:
            seen[c_sum]=i
    
    return final            
    


nums = [1,4,-5,4,6,5,-3,-3,-7,4]
K = 3
print(longest_subarray(nums,K))
            