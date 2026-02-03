def largest_element(n,nums):
    maxm=nums[0]
    for num in nums:
        if num>maxm:
            maxm=num
    return maxm
    
    
    
a=int(input("Enter total numbers:"))
b=list(map(int,input(f"Enter {a} numbers:").split()))
print(largest_element(a,b))
