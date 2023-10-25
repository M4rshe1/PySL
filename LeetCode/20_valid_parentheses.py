class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # 1. If the length of the string is odd, it is not valid
        if len(s) % 2 != 0:
            return False

        # 2. Create a stack
        stack = []

        # 3. Iterate through the string
        for char in s:
            # 4. If the char is an opening bracket, push it to the stack
            if char in ['(', '{', '[']:
                stack.append(char)
            # 5. If the char is a closing bracket, pop the stack
            else:
                if not stack:
                    return False
                top = stack.pop()
                # 6. If the popped element is not the corresponding opening bracket, return False
                if (top == '(' and char != ')') or (top == '{' and char != '}') or (top == '[' and char != ']'):
                    return False

        # 7. If the stack is empty, return True
        return not stack


isValid = Solution().isValid("()[]{)")
print(isValid)