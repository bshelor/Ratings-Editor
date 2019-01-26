#RATINGS CHANGE
import math

def getDifference(winner, loser):
    difference = winner - loser
    return difference

def getNewRatings(winner, loser):
    difference = getDifference(winner, loser)
    if difference < 0:
        higherRating = loser
        lowerRating = winner
    else:
        higherRating = winner
        lowerRating = loser

    newDiff = abs(difference)

    if newDiff in range(0, 13):
        if higherRating == loser:
            lowerRating += 8
            higherRating -= 8
        else:
            higherRating += 8
            lowerRating -= 8
    elif newDiff in range(13, 38):
        if higherRating == loser:
            higherRating -= 10
            lowerRating += 10
        else:
            higherRating += 7
            lowerRating -= 7
    elif newDiff in range(38, 63):
        if higherRating == loser:
            higherRating -= 13
            lowerRating += 13
        else:
            higherRating += 6
            lowerRating -= 6
    elif newDiff in range(63, 88):
        if higherRating == loser:
            higherRating -= 16
            lowerRating += 16
        else:
            higherRating += 5
            lowerRating -= 5
    elif newDiff in range(88, 113):
        if higherRating == loser:
            higherRating -= 20
            lowerRating += 20
        else:
            higherRating += 4
            lowerRating -= 4
    elif newDiff in range(113, 138):
        if higherRating == loser:
            higherRating -= 25
            lowerRating += 25
        else:
            higherRating += 3
            lowerRating -= 3
    elif newDiff in range(138, 163):
        if higherRating == loser:
            higherRating -= 30
            lowerRating += 30
        else:
            higherRating += 2
            lowerRating -= 2
    elif newDiff in range(163, 188):
        if higherRating == loser:
            higherRating -= 35
            lowerRating += 35
        else:
            higherRating += 2
            lowerRating -= 2
    elif newDiff in range(188, 213):
        if higherRating == loser:
            higherRating -= 40
            lowerRating += 40
        else:
            higherRating += 1
            lowerRating -= 1
    elif newDiff in range(213, 238):
        if higherRating == loser:
            higherRating -= 45
            lowerRating += 45
        else:
            higherRating += 1
            lowerRating -= 1
    else:
        if higherRating == loser:
            higherRating -= 50
            lowerRating += 50

    if difference < 0:
        loser = higherRating
        winner = lowerRating
    else:
        winner = higherRating
        loser = lowerRating
    return winner, loser

##print(getRatingChange(500,750))

def automaticMain(playerRating):
    playerWinsAgainst = input("Opponent's ratings for matches WON, separated by comma (Hit enter if none) => ")
    ratingChangeList = []
    if playerWinsAgainst != "":
        List = list(playerWinsAgainst.split(","))
        for rating in List:
            winner, loser = getNewRatings(int(playerRating), int(rating))
            difference = winner - int(playerRating)
            ratingChangeList.append(difference)

    playerLossesAgainst = input("Opponent's ratings for matches LOST, separated by comma (Hit enter if none) => ")
    if playerLossesAgainst != "":
        List = list(playerLossesAgainst.split(","))
        for ratings in List:
            winner, loser = getNewRatings(int(ratings), int(playerRating))
            difference = loser - int(playerRating)
            ratingChangeList.append(difference)

    if ratingChangeList != []:
        Rating = int(playerRating)
        for value in ratingChangeList:
            Rating += int(value)
        return Rating
    else:
        return int(playerRating)

def main():
    print("EDIT RATINGS")
    print()
    Continue = True
    while Continue:
        #TRY EXCEPT for input 
        playerRating = ""
        while playerRating == "" or int(playerRating) < 0:
            playerRating = input("Rating to edit => ")
            try:
                playerRating = int(playerRating)
            except:
                print("Number expected!")
                print()
                playerRating = ""

        playerWinsAgainst = input("Opponent's ratings for matches WON, separated by comma => ")
        List = list(playerWinsAgainst.split(","))
        ratingChangeList = []
        for rating in List:
            winner, loser = getNewRatings(int(playerRating), int(rating))
            difference = winner - int(playerRating)
            ratingChangeList.append(difference)

        playerLossesAgainst = input("Opponent's ratings for matches LOST, separated by comma => ")
        List = list(playerLossesAgainst.split(","))
        for ratings in List:
            winner, loser = getNewRatings(int(ratings), int(playerRating))
            difference = loser - int(playerRating)
            ratingChangeList.append(difference)

        Rating = int(playerRating)
        for value in ratingChangeList:
            Rating += int(value)

        print()
        print("New player rating => ", Rating)
        print()
        #TRY EXCEPT for input
        Continue = ""
        while Continue == "" or Continue not in ['y','n']:
            Continue = input("Edit more players? (y/n) => ")
            try:
                Continue = int(Continue)
                print("Letter expected!")
                print()
                Continue = ""
            except:
                Continue = Continue
                
        if Continue == "y":
            Continue = True
        else:
            Continue = False
        print()
    print("FINISHED EDITING")

##main()

def ratingChangeName(playerRating, ratingChangeList):
    if ratingChangeList != []:
        Rating = int(playerRating)
        for value in ratingChangeList:
            Rating += int(value)
        return Rating
    else:
        return int(playerRating)


          
        
        
        
        
    
    
