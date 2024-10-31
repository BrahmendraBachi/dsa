def maxArea(height):
    n = len(height)
    leftHeights, rightHeights = [0] * n, [0] * n
    maxi = 0
    for i in range(n):
        maxi = max(maxi, height[i])
        leftHeights[i] = maxi
    maxi = 0
    for i in range(n - 1, -1, -1):
        maxi = max(maxi, height[i])
        rightHeights[i] = maxi

    ptr1, ptr2 = 0, n - 1
    max_area = 0
    currArea = 0
    while ptr1 < ptr2:
        currArea = (ptr2 - ptr1) * min(leftHeights[ptr1], rightHeights[ptr2])
        max_area = max(currArea, max_area)

        tempArea1 = (ptr2 - (ptr1 + 1)) * min(leftHeights[ptr1 + 1], rightHeights[ptr2])
        tempArea2 = (ptr2 - 1 - ptr1) * min(leftHeights[ptr1], rightHeights[ptr2-1])
        if tempArea1 > tempArea2:
            ptr1 += 1
        else:
            ptr2 -= 1
    return max_area

if __name__ == "__main__":
    input1 = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    input2 = [1, 1]
    input3 = [1, 5, 6, 3, 10, 4, 3, 9]
    input4 = [2, 3, 4, 5, 18, 17, 6]
    print(maxArea(input4))
