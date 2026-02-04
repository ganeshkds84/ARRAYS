class Solution:
    def sortZeroOneTwo(self, nums):
        l = 0
        i = 0
        r = len(nums) - 1

        while i <= r:
            if nums[i] == 0:
                nums[i], nums[l] = nums[l], nums[i]
                l += 1
                i += 1

            elif nums[i] == 2:
                nums[i], nums[r] = nums[r], nums[i]
                r -= 1
                # i is NOT incremented here

            else:  # nums[i] == 1
                i += 1

        return nums

a = list(map(int, input("Enter only 0,1 and 2's: ").split()))
obj = Solution()
print(obj.sortZeroOneTwo(a))
