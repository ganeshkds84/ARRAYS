class Solution():
    def remove_duplicates(self,nums):
        i,j=0,1
        while j<len(nums):
            if nums[j]<=nums[i]:
                j+=1
            elif nums[j]>nums[i]:
                nums[i+1],nums[j]=nums[j],nums[i+1]
                i+=1
                j+=1
        return nums[:i+1]
    
a=int(input("Enter total numbers:"))
b=list(map(int,input(f"Enter {a} numbers in sorted order:").split()))
obj=Solution()
print(obj.remove_duplicates(b))
