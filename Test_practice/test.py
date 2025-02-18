def lengthOfLIS(nums):
    max_count_dict = {}
    for ind1 in range(0, len(nums)):
        inc_set = [nums[ind1]]
        max_count = 1
        for ind2 in range(ind1 + 1, len(nums)):
            if nums[ind2] > nums[ind1]:
                inc_set.append(nums[ind2])
                for ind3 in range(ind2 + 1, len(nums)):
                    if nums[ind3] > nums[ind2]:
                        inc_set.append(nums[ind3])
                        for ind4 in range(ind3 + 1, len(nums)):
                            if nums[ind4] > nums[ind3]:
                                inc_set.append(ind4)
                                for ind5 in range(ind4 + 1, len(nums)):
                                    if nums[ind5] > nums[ind4]:
                                        inc_set.append(ind5)
                                        for ind6 in range(ind5 + 1, len(nums)):
                                            if nums[ind6] > nums[ind5]:
                                                inc_set.append(ind6)
                                        max_count = max(len(inc_set), max_count)
                                        print(inc_set)
                                        inc_set.pop()
                                max_count = max(len(inc_set), max_count)
                                print(inc_set)
                                inc_set.pop()
                        max_count = max(len(inc_set), max_count)
                        print(inc_set)
                        inc_set.pop()
                max_count = max(len(inc_set), max_count)
                print(inc_set)
                inc_set.pop()
        max_count = max(len(inc_set), max_count)
        inc_set.pop()
    return


if __name__ == "__main__":
    input1 = [10, 9, 2, 5, 3, 7, 101, 18]
    input2 = [6, 2, 3, 7, 4, 5]
    print(lengthOfLIS(nums=input2))
