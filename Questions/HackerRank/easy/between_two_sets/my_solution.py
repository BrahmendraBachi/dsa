def getTotalX(a, b):
    right = min(b)
    left = max(a)
    count = 0
    for i in range(left, right + 1):
        isValid = True
        for num in a:
            if (i % num) != 0:
                isValid = False
                break
        if not isValid:
            continue
        for num in b:
            if (num % i) != 0:
                isValid = False
                break
        if not isValid:
            continue
        count += 1
    return count


if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    m = int(first_multiple_input[1])
    arr = list(map(int, input().rstrip().split()))
    brr = list(map(int, input().rstrip().split()))
    total = getTotalX(arr, brr)
