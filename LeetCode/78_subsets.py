from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def dfs(start, current_subset):
            # Add the current subset to the result
            result.append(current_subset[:])

            # Generate subsets by adding each element to the current subset
            for i in range(start, len(nums)):
                current_subset.append(nums[i])
                dfs(i + 1, current_subset)
                current_subset.pop()  # Backtrack

        result = []
        dfs(0, [])
        return result
