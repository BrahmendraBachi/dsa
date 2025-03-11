import heapq


def convert_into_max_heap(arr):
    negated_arr = [-x for x in arr]
    heapq.heapify(negated_arr)
    print(negated_arr)

    for i in range(len(arr)):
        print(heapq.heappop(negated_arr))


def convert_tuple_array_into_max_heap(arr):
    negated_arr = [(-x[0], x[1]) for x in arr]
    heapq.heapify(negated_arr)

    for i in range(len(negated_arr)):
        print(heapq.heappop(negated_arr))


def main():
    arr = [1, 2, 3, 4, 5]

    tuple_arr = [(1, "a"), (2, "b"), (3, "c"), (4, "d"), (5, "e")]

    convert_tuple_array_into_max_heap(tuple_arr)


if __name__ == "__main__":
    main()
