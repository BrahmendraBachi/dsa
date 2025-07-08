from collections import defaultdict
from typing import List


def groupAnagrams(strs: List[str]) -> List[List[str]]:
    res = defaultdict(list)

    for _str in strs:
        count = [0] * 26
        for ch in _str:
            count[ord(ch) - ord("a")] += 1

        res[tuple(count)].append(_str)

    return list(res.values())
