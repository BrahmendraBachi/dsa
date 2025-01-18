def check(arr, k, pageLimit):
    # Starting from the first student
    cnt = 1
    pageSum = 0
    for pages in arr:

        # If adding the current book exceeds the page
        # limit, assign the book to the next student
        if pageSum + pages > pageLimit:
            cnt += 1
            pageSum = pages
        else:
            pageSum += pages

    # If books can be assigned to less than k students then
    # it can be assigned to exactly k students as well
    return cnt <= k


def findPages(arr, k):
    # If number of students are more than total books
    # then allocation is not possible
    if k > len(arr):
        return -1

    # Minimum and maximum possible page limits
    minPageLimit = max(arr)
    maxPageLimit = sum(arr)

    # Iterating over all possible page limits
    for i in range(minPageLimit, maxPageLimit + 1):

        # Return the first page limit with we can
        # allocate books to all k students
        if check(arr, k, i):
            return i

    return -1


if __name__ == "__main__":
    input1 = ([3, 1, 1], 2)
    input2 = ([3, 1, 2, 1, 6], 3)
    print(findPages(input2[0], input2[1]))
    # print(find_pages(list(range(1, 31)), 10))
    # input3 =
