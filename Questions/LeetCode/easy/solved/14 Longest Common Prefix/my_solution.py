from typing import List


def longestCommonPrefix(self, strs: List[str]) -> str:
    my_prefix_word = strs[0]
    ptr = 1
    while ptr <= len(my_prefix_word):
        for rem_str in strs[1:]:
            if ptr > len(rem_str) or rem_str[:ptr] != my_prefix_word[:ptr]:
                return my_prefix_word[:ptr - 1]
        ptr += 1
    return my_prefix_word[:ptr]