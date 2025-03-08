def rotate_array(arr):
    n = len(arr)

    def shift_next(ind):
        if ind == 0:
            return arr[n - 1]
        arr[ind] = shift_next(ind - 1)
        return arr[ind]

    print(arr)


def main():
    pass


if __name__ == "__main__":
    main()
