def longestValidParentheses(self, s: str) -> int:
    longest_forward = longest_backward = 0
    count = 0
    stack = []
    for i in range(len(s)):
        if s[i] == "(":
            stack.append("(")
        else:
            if len(stack) and stack[-1] == "(":
                count += 2
                stack.pop()
            else:
                longest_forward = max(longest_forward, count)
                count = 0
                stack = []
    longest_forward = max(longest_forward, count)
    count = 0
    stack = []
    for i in range(len(s) - 1, -1, -1):
        if s[i] == ")":
            stack.append(")")
        else:
            if len(stack) and stack[-1] == ")":
                count += 2
                stack.pop()
            else:
                longest_backward = max(longest_backward, count)
                count = 0
                stack = []
    longest_backward = max(longest_backward, count)
    return min(longest_forward, longest_backward)