class Gowtham():
    def four_sum(self,nums,target):
        final=[]
        nums=sorted(nums)
        for i in range(len(nums)-3):
            t1=nums[i]
            if i>0 and nums[i]==nums[i-1]:
                continue
            j=i+1
            while j<len(nums)-2:
                t2=nums[j]
                if j>i+1 and nums[j]==nums[j-1]:
                    j+=1
                    continue
                k=j+1
                l=len(nums)-1
                while k<l:
                    t3=nums[k]
                    t4=nums[l]
                    req=t1+t2+t3+t4
                    
                    if req==target:
                        final.append([t1,t2,t3,t4])
                        k+=1
                        l-=1
                        while k<l and nums[k]==nums[k-1]:
                            k+=1
                        while k<l and nums[l]==nums[l+1]:
                            l-=1
                    elif req>target:
                        l-=1
                    else:
                        k+=1
                j+=1   
        return final
                
        
ansr=Gowtham()
print(ansr.four_sum([1,0,-1,0,-2,2],3))


    