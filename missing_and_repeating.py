class Solution():
    def missing_repeating(self,nums):
        n=len(nums)
        square_nums=[]
        for i in range(len(nums)):
            square_nums.append(nums[i]*nums[i])
        sum_nums=sum(nums)
        sum_square_nums=sum(square_nums)
        act_sum_nums=(n*(n+1))//2
        act_sum_square_nums=(n*(n+1)*(2*n+1))//6
        x=act_sum_nums-sum_nums
        y=(act_sum_square_nums-sum_square_nums)//x
        
        missing=(x+y)//2
        repeating=missing-x
        
        return missing,repeating
    
answer=Solution()
nums=list(map(int,input("Enter numbers:").split(" ")))
print(answer.missing_repeating(nums))