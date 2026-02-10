class Solution():
    def three_sum(self, nums):
        sorted_nums = sorted(nums)
        final = []
        n = len(sorted_nums)

        for i in range(n - 2):
            if i > 0 and sorted_nums[i] == sorted_nums[i - 1]:
                continue

            temp = sorted_nums[i]
            j = i + 1
            k = n - 1

            while j < k:
                temp2 = sorted_nums[j] + sorted_nums[k]
                total = temp + temp2

                if total == 0:
                    final.append([temp, sorted_nums[j], sorted_nums[k]])
                    j += 1
                    k -= 1

                    # 🔹 Skip duplicates for j
                    while j < k and sorted_nums[j] == sorted_nums[j - 1]:
                        j += 1

                    # 🔹 Skip duplicates for k
                    while j < k and sorted_nums[k] == sorted_nums[k + 1]:
                        k -= 1

                elif total > 0:
                    k -= 1
                else:
                    j += 1

        return final
       

a = list(map(int, input("Enter the numbers: ").split()))
threesum = Solution()
print(threesum.three_sum(a))
