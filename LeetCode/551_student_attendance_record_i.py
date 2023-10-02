class Solution(object):
    def checkRecord(self, s):
        print(s.count("A"))
        if s.count("A") > 1:
            return False
        if "LLL" in s:
            return False
        return True

if __name__ == "__main__":
    print(Solution().checkRecord("AA"))