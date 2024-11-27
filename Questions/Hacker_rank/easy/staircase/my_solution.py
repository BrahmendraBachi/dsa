def staircase(n):
    # Write your code here
    for i in range(1, n + 1):
        print(" " * (n - i), end="")
        print("#" * i)


if __name__ == '__main__':
    len_input = int(input().strip())

    staircase(len_input)
