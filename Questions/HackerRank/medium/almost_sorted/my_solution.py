def almostSorted(arr):
    # Write your code here
    # print(arr)
    if len(arr) == 2:
        if arr[0] < arr[1]:
            print("yes")
        else:
            print("yes")
            print("swap 1 2")
        return

    n = len(arr)

    min_edges = []
    max_edges = []
    for i in range(1, n - 1):
        if arr[i] > arr[i - 1] and arr[i] > arr[i + 1]:
            max_edges.append(i)
        if arr[i] < arr[i - 1] and arr[i + 1] > arr[i]:
            min_edges.append(i)
    edges = len(min_edges) + len(max_edges)
    if edges > 4:
        print("no")
    elif edges == 0:
        if arr[0] > arr[1]:
            print("yes")
            print(f"reverse {1} {n}")
        else:
            print("yes")
    elif len(min_edges) == 0:
        edge = max_edges[0]
        if arr[n - 1] > arr[edge - 1]:
            print("yes")
            if n - 1 - edge == 1:
                print(f"swap {edge + 1} {n}")
            else:
                print(f"reverse {edge + 1} {n}")

        else:
            print("no")

    elif len(max_edges) == 0:
        edge = min_edges[0]
        if arr[edge + 1] > arr[0]:
            print("yes")
            if edge == 1:
                print(f"swap {1} {edge + 1}")
            else:
                print(f"reverse {1} {edge + 1}")
    else:
        # print("got it")
        if len(min_edges) == 2 and len(max_edges) == 2:
            if abs(min_edges[0] - max_edges[0]) != 1 or abs(min_edges[1] - max_edges[1] != 1):
                print("no")
                return
        for edge_min in min_edges:
            for edge_max in max_edges:
                if arr[edge_min] > arr[edge_max - 1] and arr[edge_max] < arr[edge_min + 1]:
                    print("yes")
                    if abs(edge_min - edge_max) == 1 or len(min_edges) > 1:
                        print(f"swap {edge_max + 1} {edge_min + 1}")
                    else:
                        print(f"reverse {edge_max + 1} {edge_min + 1}")
                    return
        print("no")


if __name__ == '__main__':
    inp_n = int(input().strip())
    inp_arr = list(map(int, input().rstrip().split()))
    almostSorted(inp_arr)
