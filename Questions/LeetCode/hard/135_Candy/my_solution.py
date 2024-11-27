def candy(ratings):
    n = len(ratings)
    dp = [1] * n
    for i in range(1, n):
        if ratings[i] > ratings[i - 1] and not dp[i] > dp[i - 1]:
            dp[i] = dp[i - 1] + 1
        if ratings[i] < ratings[i - 1] and not dp[i] < dp[i - 1]:
            dp[i - 1] = dp[i] + 1

    for i in range(n - 2, -1, -1):
        if ratings[i] > ratings[i + 1] and not dp[i] > dp[i + 1]:
            dp[i] = dp[i + 1] + 1
        if ratings[i] < ratings[i + 1] and not dp[i] < dp[i + 1]:
            dp[i + 1] = dp[i] + 1

    return sum(dp)


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
