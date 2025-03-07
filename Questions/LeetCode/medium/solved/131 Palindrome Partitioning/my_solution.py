from typing import List


def partition(s: str) -> List[List[str]]:
    n = len(s)
    res = []

    def is_palindrome(curr_str):
        return curr_str == curr_str[::-1]

    def palindromic_partition(ind, curr_par):
        if ind >= n:
            res.append(curr_par)
            return

        for i in range(ind, n):
            if not is_palindrome(s[ind: i + 1]):
                continue
            palindromic_partition(i + 1, curr_par + [s[ind: i + 1]])

    palindromic_partition(0, [])
    return res
