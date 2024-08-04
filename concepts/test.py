def minRequiredJumps(steps):
    min_count = temp = 1000000000
    min_counts_dict = {}

    # def jumpsRequired(curr_step, count):
    #     nonlocal min_count
    #     nonlocal min_counts_dict
    #     if curr_step == len(steps) - 1:
    #         min_count = min(min_count, count)
    #         return
    #     start = curr_step + 1
    #     end = start + steps[curr_step]
    #     for next_step in range(start, min(end, len(steps))):
    #         if curr_step in min_counts_dict:
    #             min_count = min(min_count, count)
    #         count += 1
    #         jumpsRequired(next_step, count)
    #         min_counts_dict[curr_step] = count
    #         count -= 1
    #
    # jumpsRequired(0, 0)
    # return min_count if min_count != temp else 0
    min_counts = [0] * len(steps)
    for start in range(len(steps) - 2, -1, -1):
        if steps[start] == 0:
            min_counts[start] = 1000000
            continue
        end = start + steps[start] + 1
        min_counts[start] = 1 + min(min_counts[start + 1: end])
    return min_counts[0]

    # for curr_step in range(start + 1, min(len(steps), end)):
    #     if curr_step in min_counts_dict:
    #         min_counts_dict[start] = count + min_counts_dict[curr_step]
    #         min_count = min(min_count, count + min_counts_dict[start])
    #         continue
    #     if curr_step == len(steps) - 1:
    #         min_counts_dict[start] = count
    #         min_count = min(min_count, count)
    #         break
    #     count += 1


if __name__ == '__main__':
    input_1 = [2, 3, 1, 1, 4]
    input_2 = [2, 3, 0, 1, 4]
    input_3 = [4, 2, 1, 0, 4]
    input_4 = [5, 9, 3, 2, 1, 0, 2, 3, 3, 1, 0, 0]
    input_5 = [5, 6, 4, 4, 6, 9, 4, 4, 7, 4, 4, 8, 2, 6, 8, 1, 5, 9, 6, 5, 2, 7, 9, 7, 9, 6, 9, 4, 1, 6, 8, 8, 4, 4, 2,
               0, 3, 8, 5]
    print(minRequiredJumps(input_4))
