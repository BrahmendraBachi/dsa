def candy(ratings):
    def count(n):
        return (n * (n + 1)) // 2

    children = len(ratings)
    candies, i = 0, 1
    while i < children:
        inc = dec = 0
        while i < children and ratings[i] > ratings[i - 1]:
            inc += 1
            i += 1
        while i < children and ratings[i] < ratings[i - 1]:
            dec += 1
            i += 1
        if inc or dec:
            candies += count(inc - 1) + max(inc, dec) + count(dec - 1)
            continue
        i += 1
    return candies + children


if __name__ == '__main__':
    test_case1 = [1, 0, 2]
    test_case2 = [1, 2, 2]
    test_case3 = [1, 2, 3, 4, 4, 4, 4]
    test_case4 = [1, 2, 3, 4, 3, 2, 1]

    expected_outputs = [5, 4, 13, 16]
    output1 = candy(test_case1)
    output2 = candy(test_case2)
    output3 = candy(test_case3)
    output4 = candy(test_case4)

    assert expected_outputs[0] == output1
    assert expected_outputs[1] == output2
    assert expected_outputs[2] == output3
    assert expected_outputs[3] == output4

    print("\nTestCases passed successfully\n")

    print('output1: ', output1)
    print('output2: ', output2)
    print('output3: ', output3)
    print('output4: ', output4)
