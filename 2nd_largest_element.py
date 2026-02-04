def second_element(nums):
    if len(nums)<2:
        return -1
    maxm1=float('-inf')
    maxm2=float('-inf')
    for i,num in enumerate(nums):
        if num>maxm1:
            maxm2=maxm1
            maxm1=num
        elif num>maxm2 and num!=maxm1:
            maxm2=num
        #print(maxm1)
    return maxm2 if maxm2!=float('-inf') else -1
    
    
a=int(input("Enter total numbers:"))
b=list(map(int,input(f"Enter {a} numbers").split()))
print(second_element(b))