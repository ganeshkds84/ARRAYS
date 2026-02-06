class Solution():
    def majority_element(self,nums):
        m1=None
        m2=None
        c1=0
        c2=0
        for num in nums:
            if c1==0:
                m1=num
                c1=1
            elif c2==0 and m1!=num:
                m2=num
                c2=1
            elif m1==num:
                c1+=1
            elif m2==num:
                c2+=1
            else:
                c1-=1
                c2-=1
        c1,c2=0,0
        for num in nums:
            if num==m1:
                c1+=1
            elif num==m2:
                c2+=1
        result=[]
        if c1>len(nums)//3:
            result.append(m1)
        if c2>len(nums)//3:
            result.append(m2)
        return result
    

a=int(input("Enter list size:"))        
b=list(map(int,input("Enter the numbers:").split()))
ans=Solution()
print(ans.majority_element(b))