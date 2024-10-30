def threeSumClosest(nums, target):
    nums.sort()
    closest = None
    closest_sum = 0
    for i in range(len(nums) - 2):
        curr_sum = nums[i]
        l = i + 1
        r = len(nums) - 1
        while l < r:
            curr_sum += nums[r] + nums[l]
            curr_closest = target - curr_sum
            if closest is None or abs(curr_closest) < closest:
                closest = abs(curr_closest)
                closest_sum = curr_sum
            if curr_closest == 0:
                return curr_sum
            elif curr_closest > 0:
                l += 1
            else:
                r -= 1

            curr_sum = nums[i]
    return closest_sum

if __name__ == "__main__":
    input1 = [-1, 2, 1, -4]
    target1 = 1
    # print(threeSumClosest(input1, target1))

    input2 = [0, 0, 0]
    target2 = 1
    # print(threeSumClosest(input2, target2))

    input3 = [-3, -2, 4, 1, 2, 5]
    target3 = 1
    # print(threeSumClosest(input3, target3))

    input4 = [-1000,-5,-5,-5,-5,-5,-5,-1,-1,-1]
    target4 = -14
    print(threeSumClosest(input4, target4))