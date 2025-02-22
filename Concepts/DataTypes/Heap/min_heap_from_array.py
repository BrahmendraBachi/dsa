class Heap:
    def __init__(self, arr):
        self.arr = arr
        self.convert_into_heap()

    def convert_into_heap(self):
        n = len(self.arr)
        for i in range(n // 2 - 1, -1, -1):
            self.heapify(i, n)

    def heapify(self, i, n):
        arr = self.arr
        smallest = i

        left, right = 2 * i + 1, 2 * i + 2
        if left < n and self.arr[left] < arr[smallest]:
            smallest = left
        if right < n and arr[right] < arr[smallest]:
            smallest = right
        if smallest != i:
            arr[smallest], arr[i] = arr[i], arr[smallest]
            self.heapify(smallest, n)

    def add_to_heap(self, val):
        arr = self.arr
        arr.append(val)
        n = len(arr)
        ind = n - 1
        parent = (ind - 1) // 2
        isValidParent = arr[parent] <= arr[ind]
        while not isValidParent:
            arr[parent], arr[ind] = arr[ind], arr[parent]
            ind = parent
            parent = (ind - 1) // 2
            isValidParent = arr[parent] < arr[ind]
        self.heapify(ind, n)

    def pop(self):
        if len(self.arr) == 0:
            return
        root = self.arr[0]
        self.arr[0], self.arr[-1] = self.arr[-1], self.arr[0]
        self.arr.pop()
        self.heapify(0, len(self.arr))
        return root

    def print_heap(self):
        for num in self.arr[:-1]:
            print(num, end=", ")
        print(self.arr[-1])


if __name__ == "__main__":
    input_arr = [5, 3, 8, 4, 0, 6, 9, 2]
    heap_arr = Heap(input_arr)

    heap_arr.add_to_heap(1)
    heap_arr.print_heap()

    heap_arr.pop()
    heap_arr.print_heap()

    # heap_arr.add_to_heap(6)
    # heap_arr.print_heap()
