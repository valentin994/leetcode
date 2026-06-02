class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        curr = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[curr]:
                curr += 1
                nums[curr] = nums[i]
        return curr + 1


# nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
nums = [1, 2, 2]
s = Solution()

print(s.removeDuplicates(nums))
print(nums)
