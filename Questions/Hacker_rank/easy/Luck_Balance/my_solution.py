def luckBalance(k, contests):
    must_wins, lucks, max_luck = [], [], 0
    for contest in contests:
        if contest[1] == 1:
            must_wins.append(contest[0])
        lucks.append(contest[0])
    lucks.sort()
    must_wins.sort()
    while len(lucks):
        if not len(must_wins):
            max_luck += sum(lucks)
            return max_luck
        must_win = must_wins[-1]
        highest_luck = lucks.pop()
        if must_win == highest_luck:
            if k > 0:
                max_luck += must_win
                k -= 1
            else:
                max_luck -= must_win
            must_wins.pop()
            continue
        max_luck += highest_luck
    return max_luck - sum(must_wins)