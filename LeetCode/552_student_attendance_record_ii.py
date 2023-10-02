# TODO Fix this code, it's not working
class Solution(object):
    def checkRecord(self, n):
        chars = ("A", "L", "P")

        def dfs(start, current_subset):
            # Add the current subset to the result
            if len(current_subset) == n:
                result.append(current_subset)
                return
            # Add each char to the current subset
            for char in chars:
                # If the current subset is valid, add the char to it
                if (char == "P" or len(current_subset) < 2 or
                        current_subset[-1] != "L" or current_subset[-2] != "L"):
                    dfs(start + 1, current_subset + [char])

        result = []
        dfs(0, [])
        return len(result) % (10 ** 9 + 7)


if __name__ == "__main__":
    print(Solution().checkRecord(2))  # 8
    print(Solution().checkRecord(1))  # 3
    print(Solution().checkRecord(10101))  # 183236316
