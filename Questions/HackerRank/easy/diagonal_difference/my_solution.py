import os


def diagonalDifference(arr):
    # Write your code here
    len_arr = len(arr)
    d1, d2 = 0, 0
    for i in range(len_arr):
        d1 += arr[i][i]
        d2 += arr[i][len_arr - i - 1]
    return abs(d1 - d2)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input().strip())
    input_1 = []
    for _ in range(n):
        input_1.append(list(map(int, input().rstrip().split())))
    result = diagonalDifference(input_1)
    fptr.write(str(result) + '\n')
    fptr.close()
