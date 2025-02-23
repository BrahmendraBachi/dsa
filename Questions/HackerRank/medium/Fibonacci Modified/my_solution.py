def fibonacciModified(t1, t2, n):
    # Write your code here
    fibb_dict = {}

    def recursive_fibonacci(num):
        if num in fibb_dict:
            return fibb_dict[num]
        if num == 0:
            return t1
        if num == 1:
            return t2
        fibb_dict[num] = (recursive_fibonacci(num - 1) ** 2) + recursive_fibonacci(num - 2)
        return fibb_dict[num]

    return recursive_fibonacci(n - 1)
