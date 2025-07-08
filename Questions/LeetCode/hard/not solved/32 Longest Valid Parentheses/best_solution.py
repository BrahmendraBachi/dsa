
# Fails "))))())()()(()"
def longestValidParentheses(s: str) -> int:
    longest = 0
    left = right = 0
    for ch in s:
        if ch == "(":
            left += 1
        else:
            right += 1
        if left == right:
            longest = max(left * 2, longest)
        if right > left:
            left = right = 0

    left = right = 0
    for ch in list(s)[::-1]:
        if ch == "(":
            left += 1
        else:
            right += 1
        if left == right:
            longest = max(left * 2, longest)
        if left > right:
            left = right = 0

    return longest
