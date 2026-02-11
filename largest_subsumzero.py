class Solution():
    def largest_subsum(self,nums):
        seen={}
        c_sum=0
        m_len=0
        for i in range(len(nums)):
            c_sum=nums[i]+c_sum
            if c_sum==0:
                m_len=i+1
                
            elif c_sum  in seen:
                length=i-seen[c_sum]
                if length>m_len:
                    m_len=length

            else:
                seen[c_sum]=i
        
        return m_len
        
#a=list(map(int,input("Enter any numbers:").split()))        
ansr=Solution()
print(ansr.largest_subsum([-15,-2,2,-8,1,7,10,23]))