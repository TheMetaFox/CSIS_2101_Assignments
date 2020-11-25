#File:    gymScores.py 
#Project: CSIS2101 
#Author:  Joshua Peters 
#History: Version 0.0 October 14, 2020

# This program's functionis to calculate the area of a triangle.

def main():
    scores = [9.3, 9.6, 9.4, 5.0, 10.0, 9.0, 9.8, 8.8]
#    print(scores)


    finalScore = calcGymScore(scores)
#    print(len(scores))
    print(f"The average core of the team: ~{finalScore:,.1f}")

## This function uses the scores given to calculate the final score
def calcGymScore(scores):
    maxscore = max(scores)
    minscore = min(scores)
#    print(maxscore)
#    print(minscore)

#remove the maximum and minimum scores
    scores.remove(maxscore)
    scores.remove(minscore)
#    print(scores)

    total = 0
    for s in scores:
        total += s

#calculates the average
    finalScore = total / len(scores)

    return finalScore
