class Solution:
    def isValid(self, s: str) -> bool:
        braces = { "}": "{",
                   "]": "[",
                   ")": "(" }
        stack = []

        for i in s:
            if i in braces:
                if stack and stack[-1] == braces[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)

        return not stack