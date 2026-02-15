class Solution():
    def merge_sorted_arrays(self,nums1,nums2):
        if not nums2:
            return nums1,nums2
        
        i,j=0,0
        while i<len(nums1):
            if nums1[i]<nums2[j]:
                i+=1
            else:
                nums1[i],nums2[j]=nums2[j],nums1[i]
                l=0
                while l<len(nums2)-1:
                    if nums2[l]>nums2[l+1]:
                        nums2[l],nums2[l+1]=nums2[l+1],nums2[l]
                        l+=1
                    else:
                        break
                    
        return nums1,nums2
    
answer=Solution()
print(answer.merge_sorted_arrays([1,4,8,10],[2,3,9]))