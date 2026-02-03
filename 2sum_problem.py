def two_sum(target,nums):
    seen={}
    for i,num in enumerate(nums):
        temp=target-num
        if temp in seen:
            return i,seen[temp]
        seen[num]=i
            

a=int(input("How many numbers:"))
b=list(map(int,input("Enter numbers:").split()))
c=int(input("Enter the required value:"))
print(two_sum(c,b))

