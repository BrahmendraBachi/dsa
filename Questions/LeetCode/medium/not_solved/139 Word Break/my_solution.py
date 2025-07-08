from typing import List


# recursive approach
def wordBreak(s: str, wordDict: List[str]) -> bool:
    wordDict = set(wordDict)

    def can_segment(i, j, count=1):
        if i >= len(s):
            return True

        while True:
            if j > len(s): return False
            if s[i:j] not in wordDict:
                j += 1
                count += 1
                continue
            break
        return can_segment(j, j + 1) or can_segment(i, j + 1)

    return can_segment(0, 1)
