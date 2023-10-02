class Solution:
    def findComplement(self, num: int) -> int:
        binary = bin(num)[2:]
        complement = ''
        for i in binary:
            if i == '0':
                complement += '1'
            else:
                complement += '0'
        return int(complement, 2)
