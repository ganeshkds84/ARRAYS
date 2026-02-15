class Stock():
    def buy_and_sell(self,nums):
        profit=0
        buy=nums[0]
        sell=nums[0]
        i,j=0,1
        while j<len(nums):
            if nums[j]<=nums[i]:
                buy=nums[j]
                sell=nums[j]
                i=j
                j+=1
            elif nums[j]>nums[i]:
                result=nums[j]-buy
                j+=1
                if result>profit:
                    profit=result
        
        return profit
    
    
gain=Stock()
print(gain.buy_and_sell([7,6,4,3,1]))