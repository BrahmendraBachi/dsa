def move_arr(arr, index=None):
    print(arr)
    if index == 0:
        return arr[0]
    if index is None:
        index = 0
    val = arr[index]
    arr[index] = move_arr(arr, (index + 1) if index + 1 < len(arr) else 0)
    return val


if __name__ == "__main__":
    input1 = [1, 2, 3, 4, 5]
    move_arr(input1)
    print(input1)
