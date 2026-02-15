class Solution():
    def merge_overlap(self,nums):
        if not nums:
            return []

        nums.sort()
        final = [nums[0]]

        for i in range(1, len(nums)):
            last = final[-1]
            print(last[1])

            if nums[i][0] <= last[1]:  # overlap
                last[1] = max(last[1], nums[i][1])
            else:
                final.append(nums[i])

        return final
answer=Solution()
print(answer.merge_overlap([[1,3],[2,6],[8,10],[15,18]]))