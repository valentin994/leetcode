class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        pop_counter = 0
        if len(nums) <= 1:
            return 1
        for i in range(len(nums)):
            if i == 0:
                continue
            cursor = nums[i - 1]
            if cursor != nums[i]:
                pop_counter += 1
                nums[pop_counter] = nums[i]
        if nums[pop_counter + 1] != nums[len(nums) - 1]:
            nums[pop_counter + 1] = nums[len(nums) - 1]
            pop_counter += 1
        if pop_counter == 0 and len(nums) == 2:
            nums[1] = -1
        if pop_counter == 0:
            return len(nums)
        return pop_counter + 1


nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
# nums = [1, 1]
s = Solution()

print(s.removeDuplicates(nums))
print(nums)
