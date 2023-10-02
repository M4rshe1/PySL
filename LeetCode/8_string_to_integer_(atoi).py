class Solution:
    def myAtoi(self, s: str) -> int:
        for i in range(len(s)):
            if s[i] != " ":
                s = s[i:]
                break
        if len(s) == 0:
            return 0
        if s[0] == "-":
            sign = -1
            s = s[1:]
        elif s[0] == "+":
            sign = 1
            s = s[1:]
        else:
            sign = 1
        if len(s) == 0:
            return 0
        if not s[0].isdigit():
            return 0
        for i in range(len(s)):
            if not s[i].isdigit():
                s = s[:i]
                break
        if len(s) == 0:
            return 0
        if sign == 1:
            if int(s) > 2 ** 31 - 1:
                return 2 ** 31 - 1
            else:
                return int(s)
        else:
            if int(s) > 2 ** 31:
                return -2 ** 31
            else:
                return -int(s)
