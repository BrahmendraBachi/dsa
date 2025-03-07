def isPalindrome(s: str) -> bool:
    n = len(s)
    left_ptr, right_ptr = 0, n - 1
    while left_ptr < right_ptr:
        left, right = s[left_ptr], s[right_ptr]
        print(left, right)
        order_left = ord(left)
        order_right = ord(right)

        if not (0 <= order_left - ord('a') < 26 or 0 <= order_left - ord('A') < 26) and not 0 <= order_left - ord(
                '0') < 10:
            left_ptr += 1
            continue
        elif 0 <= order_left - ord('A') < 26:
            left = left.lower()

        if not (0 <= order_right - ord('a') < 26 or 0 <= order_right - ord('A') < 26) and not 0 <= order_right - ord(
                '0') < 10:
            right_ptr -= 1
            continue
        elif 0 <= order_right - ord('A') < 26:
            right = right.lower()

        if left != right:
            return False
        left_ptr += 1
        right_ptr -= 1

    return True
