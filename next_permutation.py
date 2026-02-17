class Solution():
    def next_permutation(self,nums):
        j=len(nums)-1
        while j>0 and nums[j]<=nums[j-1]:
            j-=1
            if j==0:
                i=0
                j=len(nums)-1
                while i<j:
                    nums[i],nums[j]=nums[j],nums[i]
                    i+=1
                    j-=1
                return nums
        start=j-1
        i=j
        while  i<len(nums) and nums[start]<nums[i] :
            i+=1
        end=i-1
        
        nums[start],nums[end]=nums[end],nums[start]
        i,j=start+1,len(nums)-1
        while i<j:
            nums[i],nums[j]=nums[j],nums[i]
            i+=1
            j-=1

        return nums  
    
answer=Solution()
print(answer.next_permutation([5,1,1]))