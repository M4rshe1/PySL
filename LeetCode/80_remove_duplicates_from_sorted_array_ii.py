from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return len(nums)

        unique_count = 2  # Keep at most 2 occurrences of each number

        for i in range(2, len(nums)):
            if nums[i] != nums[unique_count - 2]:
                nums[unique_count] = nums[i]
                unique_count += 1

        return unique_count


if __name__ == "__main__":
    print(Solution().removeDuplicates([1, 1, 1]))