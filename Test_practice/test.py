def lengthOfLIS(nums):

    def calculate_max_count(start=0, max_count=None):
        if max_count is None:
            max_count = {}
        if start == len(nums) - 1:
            return 0
        if nums[start] in max_count:
            return max_count[nums[start]]
        for i in range(start + 1, len(nums)):
            count = 1
            if nums[i] > nums[start]:
                count += 1 + calculate_max_count(i, max_count)
            else:
                count += calculate_max_count(i, max_count)
                if nums[i] in max_count:
                    max_count[nums[i]] = max(max_count[nums[i]], count)
                else:
                    max_count[nums[i]] = count
    calculate_max_count(0)

if __name__ == "__main__":
    input1 = [10, 9, 2, 5, 3, 7, 101, 18]
    input2 = [5, 2, 3, 6, 4]
    print(lengthOfLIS(nums=input2))
