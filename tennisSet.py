#In tennis, a set is finished when one of the players wins 6 games and the other one wins less than 5, or,
# if both players win at least 5 games, until one of the players wins 7 games.

#Determine if it is possible for a tennis set to be finished with the score score1 : score2.


def tennisSet(score1, score2):
    if (score1 ==7 or score2==7) and (5<=score1<7 or 5<=score2<7):
        return True
    elif (score1==6 or score2==6) and sum([(score1+score2)])<=10:
        return True
    else:
        return False