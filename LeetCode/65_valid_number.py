import re

pattern = r"[+-]?(?:\d+\.\d*|\.\d+|\d+)(?:[eE][+-]?\d+)?"

text = ["2", "0089", "-0.1", "+3.14", "4.", "-.9", "2e10", "-90E3", "3e+7", "+6e-1", "53.5e93", "-123.456e789"]


class Solution:
    def isNumber(self, s: str) -> bool:
        for num in text:
            return re.fullmatch(pattern, num) is not None
