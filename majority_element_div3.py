class Solution():
    def majority_element(self,nums):
        seen={}
        final=[]
        for num in nums:
            if num not in seen:
                seen[num]=1
            else:
                seen[num]=seen[num]+1
        for i in seen:
            if seen[i]>len(nums)//3:
                final.append(i)
        
        return final
    
a=int(input("Enter list size:"))        
b=list(map(int,input("Enter the numbers:").split()))
ans=Solution()
print(ans.majority_element(b))