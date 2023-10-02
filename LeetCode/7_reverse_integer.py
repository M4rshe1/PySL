class Solution:
    def reverse(self, x: int) -> int:
        var = str(x)[::-1]
        if var[-1] == '-':
            var = int('-' + var[:-1])
        else:
            var = int(var)
        if var > 2**31 - 1 or var < -2**31:
            return 0
        return var

