import os


def kangaroo(x1, v1, x2, v2):
    if v1 == v2:
        return "YES" if x1 == x2 else "NO"
    meet = (x1 - x2) / (v2 - v1)

    if 0 < meet == int(meet):
        return "YES"
    else:
        return "NO"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    first_multiple_input = input().rstrip().split()
    inp_x1 = int(first_multiple_input[0])
    inp_v1 = int(first_multiple_input[1])
    inp_x2 = int(first_multiple_input[2])
    inp_v2 = int(first_multiple_input[3])
    result = kangaroo(inp_x1, inp_v1, inp_x2, inp_v2)
    fptr.write(result + '\n')
    fptr.close()
