def kaprekar_numbers(p, q):
    # Write your code here
    count = 0
    for num in range(p, q + 1):
        sq = str(num ** 2)
        length = len(sq)
        if length == 1:
            if num > 1:
                continue
            print(num, end=" ")
            count += 1
            continue
        l = sq[: length // 2]
        r = sq[length // 2:]

        if int(l) + int(r) == num:
            print(num, end=" ")
            count += 1
    if count == 0:
        print("INVALID RANGE")


if __name__ == '__main__':
    inp_p = int(input().strip())
    inp_q = int(input().strip())
    kaprekar_numbers(inp_p, inp_q)
