def myAtoi(self, s: str) -> int:
    opp = ""
    read_number = ""
    for ch in s:
        if ch == " ":
            if read_number == "" and opp == "":
                continue
            break
        elif ch == "-" or ch == "+":
            if read_number == "" and opp == "":
                opp = ch
            else:
                break
        elif not ch.isdigit():
            break
        else:
            read_number += ch
    min_bound, max_bound = -2 ** 31, (2 ** 31) - 1
    if read_number != "":
        if opp == "-":
            return max(-1 * int(read_number), min_bound)
        return min(int(read_number), max_bound)
    return 0
