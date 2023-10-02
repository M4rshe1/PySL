from typing import List


class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        count = 0
        for i in words:
            if s.startswith(i):
                if i == s:
                    pass
                count += 1
        return count


if __name__ == '__main__':
    Solution().countPrefixes(["a","b","c","ab","bc","abc"], "abc")