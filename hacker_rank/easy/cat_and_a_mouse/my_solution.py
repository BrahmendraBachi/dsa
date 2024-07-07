import os


def catAndMouse(x, y, z):
    if abs(x - z) == abs(y - z):
        return "Mouse C"
    if abs(x - z) < abs(y - z):
        return "Cat A"
    return "Cat B"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    q = int(input())
    for q_itr in range(q):
        xyz = input().split()
        inp_x = int(xyz[0])
        inp_y = int(xyz[1])
        inp_z = int(xyz[2])
        result = catAndMouse(inp_x, inp_y, inp_z)
        fptr.write(result + '\n')
    fptr.close()
