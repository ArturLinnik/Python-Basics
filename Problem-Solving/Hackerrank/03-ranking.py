
# Given a ranking and the scores of a player return the position in the ranking for each of the scores.

from bisect import bisect_right

def climbingLeaderboard(ranked, player):

    ranked = sorted(set(ranked))

    ranking = []

    for i in player:
        magic_number = bisect_right(ranked,i)
        ranking.append(len(ranked)-magic_number+1)

    return ranking

array_ranked = [100,100,50,40,40,20,10]
array_player = [5,25,50,120]

print(climbingLeaderboard(array_ranked,array_player))
