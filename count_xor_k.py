class Solution():
    def count_xor(self,nums,k):
        final=[]
        for i in range(len(nums)):
            result=nums[i]
            if result==k:
                final.append([result])
            for j in range(i+1,len(nums)):
                result=result^nums[j]
                if result==k:
                    final.append(nums[i:j+1])

                
        return len(final)
answer=Solution()
print(answer.count_xor([4,2,2,6,4],6))

