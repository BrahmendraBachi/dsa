def miniMaxSum(arr):
    arr.sort()
    print(sum(arr[0:4]), sum(arr[1:5]))


if __name__ == '__main__':
    input_1 = list(map(int, input().rstrip().split()))
    miniMaxSum(input_1)
