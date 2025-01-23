

def permutations(nums, start=0):
    perms = []
    if start == len(nums):
        return [nums]

    for i in range(start, len(nums)):
        words = nums.copy()
        words[i], words[start] = swap(words[i], words[start])
        perms += permutations(words, start=start+1)
    return perms

        
def swap(a, b):
    return b, a



if __name__ == "__main__":
    all_perms = permutations(["a", "b", "c", "d"], start=0)
    print(all_perms)
    print(len(all_perms))













