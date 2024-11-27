import os


def circularArrayRotation(a, k, queries):
    # Write your code here
    # for i in range(k):
    #     ele = a.pop()
    #     a.insert(0, ele)
    n = len(a)
    k = k % n
    a = a[n - k:] + a[:n - k]
    res = []
    for query in queries:
        if query >= len(a):
            continue
        res.append(a[query])
    return res


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    first_multiple_input = input().rstrip().split()
    inp_n = int(first_multiple_input[0])
    inp_k = int(first_multiple_input[1])
    q = int(first_multiple_input[2])
    inp_a = list(map(int, input().rstrip().split()))
    inp_queries = []
    for _ in range(q):
        queries_item = int(input().strip())
        inp_queries.append(queries_item)

    result = circularArrayRotation(inp_a, inp_k, inp_queries)
    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')
    fptr.close()
