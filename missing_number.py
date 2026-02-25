class Solution():
    def missing_number(self,nums):
        n=len(nums)
        req=sum(nums)
        missing=(n*(n+1))/2-req
        return int(missing)
        pass
    
    
a=[9,6,4,2,3,5,7,0,1]
answer=Solution()
print(answer.missing_number(a))