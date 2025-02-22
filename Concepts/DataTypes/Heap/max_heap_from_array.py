class Max_Heap:
    def __init__(self, arr):
        self.arr = arr
        self.convert_into_heap()

    def convert_into_heap(self):
        arr = self.arr
        n = len(arr)
        for i in range((n // 2) - 1, -1, -1):
            self.heapify(i, n)

    def heapify(self, i, n):
        arr = self.arr
        largest = i
        left, right = (2 * i) + 1, (2 * i) + 2
        if left < n and arr[left] > arr[largest]:
            largest = left
        if right < n and arr[right] > arr[largest]:
            largest = right
        if largest != i:
            arr[largest], arr[i] = arr[i], arr[largest]
            self.heapify(largest, n)

    def sort(self):
        arr = self.arr
        n = len(self.arr)
        for i in range(n - 1, -1, -1):
            arr[i], arr[0] = arr[0], arr[i]
            self.heapify(0, i)

    def print_heap(self):
        for num in self.arr[:-1]:
            print(num, end=", ")
        print(self.arr[-1])


if __name__ == "__main__":
    input_arr = [5, 3, 8, 4, 1, 6, 9, 2]
    max_heap = Max_Heap(input_arr)
    max_heap.print_heap()

    max_heap.sort()
    max_heap.print_heap()