class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        if target < nums[0]:
            return 0
        if target > nums[-1]:
            return len(nums)
        for i, k in enumerate(nums):
            if k == target:
                return i
            if i < len(nums) - 1 and k < target < nums[i + 1]:
                return i + 1


if __name__ == "__main__":
    print(Solution().searchInsert([1,3,5,7], 6))