class Solution(object):
    def reverseWords(self, s):
        arr = []
        for i in s.split():
            arr.append(i[::-1])
        return " ".join(arr)


if __name__ == "__main__":
    s = Solution()
    print(s.reverseWords("Let's take LeetCode contest"))
    print(s.reverseWords("God Ding"))
