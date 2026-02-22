class Solution():
    def spiral_matrix(self,nums,row,col):
        final=[]
        r,b=0,row-1
        l,t=col-1,0
        temp=0
        for k in range(2):
            #temp=0
            while temp<=b:
                final.append(nums[r][temp])
                temp+=1
            r+=1
            temp=r
            while temp<=l:
                final.append(nums[temp][b])
                temp+=1
            b-=1
            temp=b
            while temp>=t:
                final.append(nums[l][temp])
                temp-=1
            l-=1
            temp=l
            while temp>0:
                final.append(nums[temp][t])
                temp-=1
            t+=1
            temp=t
        
        return final
    
a=[
 [5,1,9,11],
 [2,4,8,10],
 [13,3,6,7],
 [15,14,12,16]
]
answer=Solution()
print(answer.spiral_matrix(a,4,4))