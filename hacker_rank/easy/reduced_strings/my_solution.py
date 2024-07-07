import os


def superReducedString(s):
    # Write your code here
    n = len(s)
    s = list(s)
    i, j = 0, 1

    while i < n - 1 and j < n:
        if s[i] == s[j]:
            s.pop(j)
            s.pop(i)
            if i == 0:
                pass
            else:
                i -= 1
                j -= 1
            n -= 2
        else:
            i += 1
            j += 1
    if len(s) == 0:
        return "Empty String"
    return "".join(s)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    inp_s = input()
    result = superReducedString(inp_s)
    fptr.write(result + '\n')
    fptr.close()
