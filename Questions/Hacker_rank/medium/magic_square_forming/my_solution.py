import os


def check(s):
    s1 = s[0][0] + s[1][1] + s[2][2]
    s2 = s[2][0] + s[1][1] + s[0][2]
    s3 = s[0][0] + s[1][0] + s[2][0]
    s4 = s[0][1] + s[1][1] + s[2][1]
    s5 = s[0][2] + s[1][2] + s[2][2]
    s6, s7, s8 = sum(s[0]), sum(s[1]), sum(s[2])

    checkList = [s1, s2, s3, s4, s5, s6, s7, s8]
    for i in checkList:
        if i != s1:
            return False
    return True


def diff(mat, s):
    count1 = 0
    for i in range(3):
        for j in range(3):
            count1 += abs(mat[i][j] - s[i][j])
    return count1


def swap(a, b):
    return b, a


def findAllPermutations(l, n, numbers, count):
    if l == n:
        mat, dum = [], []
        for i in range(9):
            if len(dum) == 3:
                mat.append(dum)
                dum = []
            dum.append(numbers[i])
        mat.append(dum)
        if check(mat):
            difValue = diff(mat, s)
            if difValue == 8:
                print(numbers)
            if count == -1 or count > difValue:
                count = difValue
        return count
    for i in range(l, n):
        numbers[i], numbers[l] = swap(numbers[i], numbers[l])
        count = findAllPermutations(l + 1, n, numbers, count)
        numbers[i], numbers[l] = swap(numbers[i], numbers[l])
    return count


def formingMagicSquare(s):
    numbers = []
    for i in range(1, 10):
        numbers.append(i)

    return findAllPermutations(0, 9, numbers, -1)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    inp_s = []
    for _ in range(3):
        inp_s.append(list(map(int, input().rstrip().split())))

    result = formingMagicSquare(s)
    fptr.write(str(result) + '\n')
    fptr.close()
