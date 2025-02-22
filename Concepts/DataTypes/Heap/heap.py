from heapq import heappush, heappop, heapify


def print_heap(arr):
    for num in arr[:-1]:
        print(num, end=", ")
    print(arr[-1])


def main():
    arr = [5, 3, 8, 4, 0, 6, 9, 2]
    heapify(arr)
    print_heap(arr)

    # pushes into heap array
    heappush(arr, 7)
    print_heap(arr)

    # pops the last element
    heappop()
    print_heap(arr)


if __name__ == "__main__":
    main()
