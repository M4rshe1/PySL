from typing import List


class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        count = 0
        tmp_count = 0
        for i, num in enumerate(nums):
            if num > 0 and num > nums[i - 1]:
                tmp_count += 1
            else:

                tmp_count = 1
            if count < tmp_count:
                count = tmp_count
        return count


if __name__ == "__main__":
    print(Solution().findLengthOfLCIS([1,3,5,4,7]))