from typing import List


class Solution(object):
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        strs.sort(key=len)
        pref = ""
        for j in range(len(strs[0])):
            char = strs[0][j]
            for i in strs:
                if i[j] != char:
                    return pref
            pref += char
        return pref


if __name__ == "__main__":
    print(Solution().longestCommonPrefix(["flower", "flow", "flight"]))
