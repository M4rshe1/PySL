class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle not in haystack:
            return -1
        else:
            return haystack.index(needle)


if __name__ == "__main__":
    # Input: haystack = "sadbutsad", needle = "sad"$
    print(Solution().strStr("sadbutsad", "sad"))