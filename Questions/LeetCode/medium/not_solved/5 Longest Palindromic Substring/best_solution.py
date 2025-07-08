def longestPalindrome(s: str) -> str:
    longest = 0
    longest_palindrome = ""

    for i in range(len(s)):
        l = r = i
        while l >= 0 and r < len(s) and s[l] == s[r]:
            if r - l + 1 > longest:
                longest = r - l + 1
                longest_palindrome = s[l: r + 1]
            l -= 1
            r += 1

    for i in range(len(s)):
        l, r = i, i + 1
        while l >= 0 and r < len(s) and s[l] == s[r]:
            if r - l + 1 > longest:
                longest = r - l + 1
                longest_palindrome = s[l: r + 1]
            l -= 1
            r += 1

    return longest_palindrome
