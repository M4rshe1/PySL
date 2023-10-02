from typing import List


class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        count = 0
        for i in words:
            if i.startswith(pref):
                count += 1
        return count



if __name__ == "__main__":
    print(Solution().prefixCount(["apple", "app", "apricot", "stone", "apocalypse"], "ap"))