import os


def biggerIsGreater(w):
    w = list(w)
    n = len(w)
    ind = -1

    # Find the largest index k such that w[k] < w[k+1]
    for i in range(n - 1, 0, -1):
        if w[i] > w[i - 1]:
            ind = i - 1
            break

    # If no such index exists, return "no answer"
    if ind == -1:
        return "no answer"

    # Find the largest index l greater than k such that w[k] < w[l]
    for j in range(n - 1, ind, -1):
        if w[j] > w[ind]:
            w[ind], w[j] = w[j], w[ind]
            break

    # Reverse the suffix starting at index k+1
    w[ind + 1:] = reversed(w[ind + 1:])
    return "".join(w)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    T = int(input().strip())
    for T_itr in range(T):
        inp_w = input()
        result = biggerIsGreater(inp_w)
        fptr.write(result + '\n')
    fptr.close()
