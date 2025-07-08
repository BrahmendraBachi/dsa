from typing import List


def wordBreak(s: str, wordDict: List[str]) -> List[str]:
    wordDict = set(wordDict)
    n = len(s)
    res = []

    def partition(ind, curr_sentence):
        if ind >= n:
            res.append(" ".join(curr_sentence))
            return

        for i in range(ind, n):
            substr = s[ind: i + 1]
            if substr not in wordDict:
                continue
            partition(i + 1, curr_sentence + [substr])

    partition(0, [])

    return res
