from typing import List


def nextPermutation(nums: List[int]) -> None:
    w = nums
    n = len(w)
    ind = -1

    # Find the largest index k such that w[k] < w[k+1]
    for i in range(n - 1, 0, -1):
        if w[i] > w[i - 1]:
            ind = i - 1
            break

    # If no such index exists, return "no answer"
    if ind == -1:
        w.sort()
        return

    # Find the largest index l greater than k such that w[k] < w[l]
    for j in range(n - 1, ind, -1):
        if w[j] > w[ind]:
            w[ind], w[j] = w[j], w[ind]
            break

    # Reverse the suffix starting at index k+1
    w[ind + 1:] = reversed(w[ind + 1:])

    return
