def longestPalindrome(s: str) -> int:
    letters_dict = {}
    for letter in s:
        letters_dict.setdefault(letter, 0)
        letters_dict[letter] += 1

    longest_palindrome = 0
    is_odd = False
    for letter, count in letters_dict.items():
        if count % 2 == 0:
            longest_palindrome += count
        else:
            is_odd = True
            longest_palindrome += count - 1

    return longest_palindrome + (1 if is_odd else 0)
