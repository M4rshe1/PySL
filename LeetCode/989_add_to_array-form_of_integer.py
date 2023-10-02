from typing import List


class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        for i in range(len(num) - 1, -1, -1):
            num[i] += k
            k, num[i] = divmod(num[i], 10)
        while k:
            k, digit = divmod(k, 10)
            num.insert(0, digit)
        return num