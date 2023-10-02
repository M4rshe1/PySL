from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Time complexity: O(n)
        Space complexity: O(n)
        """
        seen = {}
        for i, num in enumerate(nums):
            if target - num in seen:
                return [seen[target - num], i]
            seen[num] = i
        return []


if __name__ == "__main__":
    nums = [-2, 7, 11, 15]
    target = 9
    print(Solution().twoSum(nums, target))