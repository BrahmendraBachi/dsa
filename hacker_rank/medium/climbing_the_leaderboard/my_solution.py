import os


def climbingLeaderboard(ranked, player):
    ranked = list(dict.fromkeys(ranked))
    player_ranks = []
    player = player[::-1]
    r_ind, p_ind = len(ranked) - 1, len(player) - 1
    while p_ind + 1:
        if player[p_ind] < ranked[r_ind]:
            # ranked.append(player[p_ind])
            player_ranks.append(r_ind + 2)
            p_ind -= 1
        elif player[p_ind] == ranked[r_ind]:
            player_ranks.append(r_ind + 1)
            p_ind -= 1
        else:
            r_ind -= 1
            if r_ind < 0:
                player_ranks.append(1)
                p_ind -= 1
    return player_ranks


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    ranked_count = int(input().strip())
    inp_ranked = list(map(int, input().rstrip().split()))
    player_count = int(input().strip())
    inp_player = list(map(int, input().rstrip().split()))
    result = climbingLeaderboard(inp_ranked, inp_player)
    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')
    fptr.close()
