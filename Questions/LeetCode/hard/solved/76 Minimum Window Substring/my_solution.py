def minWindow(s, t):
    chrs_dict = {}
    curr_chrs_dict = {}
    for ch in t:
        if ch in chrs_dict:
            chrs_dict[ch] += 1
        else:
            chrs_dict[ch] = 1
    i = j = 0
    min_count = None
    min_windowed_string = ""
    while i < len(s) or len(chrs_dict) == 0:
        if len(chrs_dict) > 0:
            if s[i] in chrs_dict:
                if chrs_dict[s[i]] > 1:
                    chrs_dict[s[i]] -= 1
                else:
                    del chrs_dict[s[i]]
            else:
                if s[i] in curr_chrs_dict:
                    curr_chrs_dict[s[i]] += 1
                else:
                    curr_chrs_dict[s[i]] = 1
            i += 1
        else:
            if min_count is None or min_count > (i - j):
                min_count = i - j
                min_windowed_string = s[j:i]
            if s[j] in curr_chrs_dict:
                if curr_chrs_dict[s[j]] > 1:
                    curr_chrs_dict[s[j]] -= 1
                else:
                    del curr_chrs_dict[s[j]]
            else:
                if s[j] in chrs_dict:
                    chrs_dict[s[j]] += 1
                else:
                    chrs_dict[s[j]] = 1
            j += 1

    return min_windowed_string


if __name__ == "__main__":
    input1 = "AABBECABC"
    input2 = "ADOBECODEBANC"
    print(minWindow(input1, "ABC"))
    print(minWindow(input2, "ABC"))
    print(minWindow("a", "a"))
    print(minWindow("aa", "aaa"))
