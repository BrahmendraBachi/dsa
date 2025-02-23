import os


def queensAttack(n, k, r_q, c_q, obstacles):
    r1, c1 = r_q, c_q
    d1, d2, d3, d4, d5, d6, d7, d8 = -1, -1, -1, -1, -1, -1, -1, -1
    for obstacle in obstacles:

        r2, c2 = obstacle[0], obstacle[1]
        if r1 == r2:
            if c1 < c2:
                if d1 == -1 or (c2 - c1) < d1:
                    d1 = c2 - c1
            else:
                if d2 == -1 or (c1 - c2) < d2:
                    d2 = c1 - c2

        if c1 == c2:
            if r1 < r2:
                if d3 == -1 or (r2 - r1) < d3:
                    d3 = r2 - r1

            else:
                if d4 == -1 or (r1 - r2) < d4:
                    d4 = r1 - r2

        if abs(r2 - r1) == abs(c2 - c1):
            if r2 - r1 > 0 and c2 - c1 > 0:
                if d5 == -1 or (r2 - r1) < d5:
                    d5 = r2 - r1

            if r2 - r1 < 0 and c2 - c1 < 0:
                if d6 == -1 or r1 - r2 < d6:
                    d6 = r1 - r2

            if r2 - r1 > 0 > c2 - c1:
                if d7 == -1 or r2 - r1 < d7:
                    d7 = r2 - r1

            if r2 - r1 < 0 < c2 - c1:
                if d8 == -1 or c2 - c1 < d8:
                    d8 = c2 - c1

    count = 0

    print(d1, d2, d3, d4)

    count += d1 - 1 if d1 != -1 else (n - c1)
    count += d2 - 1 if d2 != -1 else (c1 - 1)
    count += d3 - 1 if d3 != -1 else (n - r1)
    count += d4 - 1 if d4 != -1 else (r1 - 1)

    if d5 != -1:
        count += d5 - 1
    else:
        count1 = 1
        while (r1 + count1 <= n) and (c1 + count1 <= n):
            count += 1
            count1 += 1

    if d6 != -1:
        count += d6 - 1
    else:
        count1 = 1
        while (r1 - count1) >= 1 and (c1 - count1) >= 1:
            count += 1
            count1 += 1

    if d7 != -1:
        count += d7 - 1
    else:
        count1 = 1
        while (r1 + count1) <= n and (c1 - count1) >= 1:
            count += 1
            count1 += 1

    if d8 != -1:
        count += d8 - 1
    else:
        count1 = 1
        while (r1 - count1) >= 1 and (c1 + count1) <= n:
            count += 1
            count1 += 1

    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    first_multiple_input = input().rstrip().split()
    inp_n = int(first_multiple_input[0])
    inp_k = int(first_multiple_input[1])
    second_multiple_input = input().rstrip().split()
    inp_r_q = int(second_multiple_input[0])
    inp_c_q = int(second_multiple_input[1])
    inp_obstacles = []
    for _ in range(inp_k):
        inp_obstacles.append(list(map(int, input().rstrip().split())))

    result = queensAttack(inp_n, inp_k, inp_r_q, inp_c_q, inp_obstacles)
    fptr.write(str(result) + '\n')
    fptr.close()
