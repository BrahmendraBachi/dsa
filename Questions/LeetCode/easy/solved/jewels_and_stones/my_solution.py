def numJewelsInStones(jewels: str, stones: str) -> int:
    let_counts = {}
    for i in stones:
        if i in let_counts:
            let_counts[i] += 1
        else:
            let_counts[i] = 1
    count = 0
    for i in jewels:
        if i in let_counts:
            count += let_counts[i]
    return count
