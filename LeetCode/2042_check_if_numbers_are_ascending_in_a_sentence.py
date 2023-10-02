class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        num = 0
        for word in s.split():
            if word.isnumeric():
                if int(word) <= num:
                    return False
                num = int(word)
        return True
