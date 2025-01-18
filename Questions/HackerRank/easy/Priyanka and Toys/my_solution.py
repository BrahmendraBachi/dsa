def toys(w):
    # Write your code here
    w.sort()
    if len(w) == 0:
        return 0
    # first_weight = w[0]
    count = 1
    max_weight = w[0] + 4
    i = 1
    while i < len(w):
        if w[i] <= max_weight:
            i += 1
            continue
        count += 1
        max_weight = w[i] + 4
    return count