###############################################################################
#**** Version_1.2 ****#
#**
#** Version Updates:
#** - fixed bug where program errored out in certain instances when using the
#**   edit all players function
#** - other minor bug fixes
#** - added comments in code
#** - minor visual updates
#**
#** Edited by: Bryson Shelor
###############################################################################

import TableTennisRatings
from TableTennisPlayers import *


def editPlayerStats(myPlayers, player):
    ratingChangeList = []
    playerRating = myPlayers.getRating(player)
    print("Editing for:", player)
    wins = 0
    losses = 0
    wksPlayed = 0
    while True:
        #TRY EXCEPT for input
        Win = "food"
        while Win == "food":
            Win = input("Win against (Hit enter to move to losses) => ")
            try:
                Win = int(Win)
                print("Name expected!")
                print()
                Win = "food"
            except:
                if Win != "":
                    if Win == player:
                        print("Can't win against yourself!")
                        print()
                        Win = "food"
                    else:
                        if not myPlayers.playerIn(Win):
                            print("Player not in database")
                            print()
                            Win = "food"
                        else:
                            Win = Win
                else:
                    Win = Win
        if Win == "":
            break
        else:
            opponentRating = int(myPlayers.getRating(Win))
            winner, loser = TableTennisRatings.getNewRatings(int(playerRating), int(opponentRating))
            difference = winner - int(playerRating)
            ratingChangeList.append(difference)
            wins += 1
            
    while True:
        #TRY EXCEPT for input
        Loss = "food"
        while Loss == "food":
            Loss = input("Loss against (Hit enter to finish) => ")
            try:
                Loss = int(Loss)
                print("Name expected!")
                print()
                Loss = "food"
            except:
                if Loss != "":
                    if Loss == player:
                        print("Can't lose against yourself!")
                        print()
                        Loss = "food"
                    else:
                        if not myPlayers.playerIn(Loss):
                            print("Player not in database")
                            print()
                            Loss = "food"
                        else:
                            Loss = Loss
                else:
                    Loss = Loss
                    
        if Loss == "":
            break
        else:
            opponentRating = int(myPlayers.getRating(Loss))
            winner, loser = TableTennisRatings.getNewRatings(opponentRating, int(playerRating))
            difference = loser - int(playerRating)
            ratingChangeList.append(difference)
            losses += 1

    if ratingChangeList != []:
        Rating = int(playerRating)
        wksPlayed += 1
        for value in ratingChangeList:
            Rating += value
    else:
        Rating = int(playerRating)

    myPlayers.editPlayerRating(player, Rating)
    myPlayers.editPlayerWins(player, myPlayers.getWins(player)+ wins)
    myPlayers.editPlayerLosses(player, myPlayers.getLosses(player)+ losses)
    myPlayers.editWksPlayed(player, myPlayers.getWksPlayed(player) + wksPlayed)
    print()
    print("Updated player:")
    print("%-20s %-8d %d %s %-5d %d %-15s" % (player, Rating, myPlayers.getWins(player), "-", myPlayers.getLosses(player), myPlayers.getWksPlayed(player), "wks played"))
    print()

    Pause = input("Hit enter to continue => ")
    while Pause != "":
        Pause = input("Hit enter to continue => ")
    
        

def editAllPlayersStats(myPlayers):
    playerList = myPlayers.getListOfActivePlayers()
    newD = {}
    goBack = False
    for player in playerList:
        newD[player] = []
        playerRating = myPlayers.getRating(player)
        print("\n\n\n")
        print("*****************************************************")
        print("***     Enter 'save' at any time to return to     ***")
        print("***     database menu and save information        ***")
        print("***     previously entered.                       ***")
        print("*****************************************************")
        print("***     Enter 'clear' at any time to return       ***")
        print("***     to databse menu without saving.           ***")
        print("*****************************************************")
        print("Editing for: ", player)
        wins = 0
        losses = 0
        wksPlayed = 0
        count = 0
        shouldSave = True
        while True:
            #TRY EXCEPT for input
            Win = "food"
            while Win == "food":
                Win = input("Win against (Hit enter to move to losses) => ")
##                print("b = Back; c = Clear; s = Save")
                try:
                    Win = int(Win)
                    print("Name expected!")
                    print()
                    Win = "food"
                except:
                    if Win != "":
                        if Win != 'save':
                            if ( Win != 'clear' ):
                                if ( Win != 'b' ):
                                    if Win == player:
                                        print("Can't win against yourself!")
                                        print()
                                        Win = "food"
                                    else:
                                        if not myPlayers.playerIn(Win):
                                            print("Player not in database")
                                            print()
                                            Win = "food"
                                        else:
                                            Win = Win
                                else:
                                    Win = Win
                            else:
                                Win = Win
                        else:
                            Win = Win
                    else:
                        Win = Win

            ## ENTERING 'save' saves previous work and exits while loop
            if Win == 'save':
                break

## *******************************************************************
            ##** \/ PROTOTYPE STAGE, currently causes errors \/ **##
## *******************************************************************
            ## ENTERING 'b' clears most previous entry
            if ( Win == 'b' ):
                if newD[player] == [] or len(newD[player]) == 3:
                    print("\n", "Can't go back!")
                else:
                    newD[player].pop(0)
                    print("\n", "Previous entry cleared", "\n")
                goBack = True
## *******************************************************************
            ##** /\               /\                /\          **##
## *******************************************************************

            ## ENTERING 'clear' exits while loop without saving previous work
            if ( Win == 'clear' ):
                shouldSave = False
                break

            if Win == "":
                ## IN CASE they hit enter and don't enter any wins, then
                ## this adds wins(0), losses(0), and wksPlayed(0) to that
                ## players list within newD.  Prevents indexing error later.
                newD[player].append(wins)
                newD[player].append(losses)
                newD[player].append(wksPlayed)
                break
            else:
                ## IF user has entered 'b' to clear previous entry, nothing
                ## is added to that players list for wins or losses
##                if ( goBack ):
                
                ## Determines amount of rating change for beating someone
                ## and adds that to the list to determine new rating
                ## after totally finished.
                opponentRating = int(myPlayers.getRating(Win))
                winner, loser = TableTennisRatings.getNewRatings(int(playerRating), int(opponentRating))
                difference = winner - int(playerRating)
                newD[player].insert(0, difference)
                wins += 1

                ## IF this is first entry, their wins, losses, and wksPlayed
                ## are all saved in the list within newD.  This prevents an
                ## indexing error later on in case they terminate the program
                ## early.
                if ( count < 1 ):
                    newD[player].append(wins)
                    newD[player].append(losses)
                    wksPlayed = 1
                    newD[player].append(wksPlayed)
                    count += 1

                else:
                    ## IF not first entry, then wins is updated after each entry
                    newD[player].pop(-3)
                    newD[player].insert(-2, wins)

        if Win == 'save':
            break

        if ( Win == 'clear' ):
            break
        
        while True:
            #TRY EXCEPT for input
            Loss = "food"
            while Loss == "food":
                Loss = input("Loss against (Hit enter to finish) => ")
                try:
                    Loss = int(Loss)
                    print("Name expected!")
                    print()
                    Loss = "food"
                except:
                    if Loss != "":
                        if Loss != 'save':
                            if ( Loss != 'clear' ):
                                if Loss == player:
                                    print("Can't lose against yourself!")
                                    print()
                                    Loss = "food"
                                else:
                                    if not myPlayers.playerIn(Loss):
                                        print("Player not in database")
                                        print()
                                        Loss = "food"
                                    else:
                                        Loss = Loss
                            else:
                                Loss = Loss
                        else:
                            Loss = Loss
                    else:
                        Loss = Loss

            ## ENTERING 'save' saves previous work and exits while loop
            if Loss == 'save':
                break

            ## ENTERING 'clear' exits while loop without saving previous work
            if ( Loss == 'clear' ):
                shouldSave = False
                break
            elif Loss == "":
                break
            else:
                opponentRating = int(myPlayers.getRating(Loss))
                winner, loser = TableTennisRatings.getNewRatings(opponentRating, int(playerRating))
                difference = loser - int(playerRating)
                newD[player].insert(0, difference)
                losses += 1
                ## UPDATES losses within that player's list
                newD[player].pop(-2)
                newD[player].insert(-1, losses)

        if Loss == 'save':
            break

        if ( Loss == 'clear' ):
            break

        if newD[player] != []:
            ## Rating is calculated and wins, losses, and wksPlayed is set
            ## to display to user.
            Rating = int(playerRating)
            if ( len(newD[player]) > 3 ):
                for value in range(0, len(newD[player])-3):
                    Rating += newD[player][value]

            wins = newD[player][-3]
            losses = newD[player][-2]
            wksPlayed = newD[player][-1]


        print()
        print("Updated player:")
        print("%-20s %-8d %d %s %-5d %d %-15s" % (player, Rating, myPlayers.getWins(player) + wins, "-", myPlayers.getLosses(player) + losses, myPlayers.getWksPlayed(player) + wksPlayed, "wks played"))
        print()

        Pause = 'food'
        while True:
            Pause = input("Hit enter to continue to next player => ")
            if Pause == "":
                break
            if Pause == 'done':
                break
        if Pause == 'done':
            break
        print()

    ## NOW FINISHED, we update each edited player's stats.  If a player has
    ## not been edited (not played), then nothing is updated.
    print(shouldSave)
    if ( shouldSave ): 
        changeAllRatings(newD, myPlayers)

        print()
        print("SAVED Progress")
        print()
        check = input("Hit enter to continue => ")
        while check != '':
            check = input("INVALID: Hit enter to continue => ")
            

def changeAllRatings(newD, myPlayers):
    #Edits ratings for all players at one time
    for player in newD:
        if newD[player] != []:
            ## IF this player has been edited, we get the W/L/Wksplayed info
            ## and update them in the database.  IF a player has not been
            ## edited, nothing is updated for them.
            Rating = myPlayers.getRating(player)
            for difference in newD[player]:
                Rating += difference
            wksPlayed = newD[player].pop(-1)
            losses = newD[player].pop(-1)
            wins = newD[player].pop(-1)

            myPlayers.editPlayerRating(player, Rating)
            myPlayers.editPlayerWins(player, myPlayers.getWins(player)+ wins)
            myPlayers.editPlayerLosses(player, myPlayers.getLosses(player)+ losses)
            myPlayers.editWksPlayed(player, myPlayers.getWksPlayed(player) + wksPlayed)
        

def showDatabaseMenu(myPlayers):
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    print("\n\n\n\n\n\n\n\n")
    print("----------------------------------------------------")
    print("Active Players:")
    myPlayers.showActivePlayers()
    print()

    print("--------DATABASE MENU--------")
    print("1) Edit player")
    print("2) Add players")
    print("3) Change active/inactive status of players")
    print("4) Update stats for ALL players")
    print("5) Reset stats for new session")
    print("6) Save database and exit")
    print("7) Save as new file and exit")
    print("8) Save for printing and exit")
    print("9) Close without saving")
    print("-----------------------------")
    print()


def changePlayerKey(whichPlayer, myPlayers):
    print()
    #TRY EXCEPT for input
    newName = ""
    while newName == "":
        newName = input("To what? => ")
        try:
            newName = int(newName)
            print("Name expected!")
            print()
            newName = ""
        except:
            newName = newName

    myPlayers.changePlayerKey(whichPlayer, newName)
    print()
    print("New name:", newName, "   ", myPlayers.getRating(newName), "   ", myPlayers.getStatus(newName))
    print()
    whichPlayer = newName
    Pause = input("Hit enter to continue => ")
    while Pause != "":
        Pause = input("INVALID: Hit enter to continue => ")
    keepGoing = ""


def displayEditPlayerStatsMenu():
    print("Edit what?")
    print("1)Rating")
    print("2)Record")
    print("3)Weeks Played")
    print("4)Back")
    print("-------------------")
    

def changePlayerRating(whichPlayer, myPlayers):
    print()
    print("Old rating:",myPlayers.getRating(whichPlayer))
    print()

    #TRY EXCEPT for input
    newRating = ""
    while newRating == "":
        newRating = input("New rating => ")
        try:
            newRating = int(newRating)
            if newRating < 0:
                print("Can't be negative!")
                newRating = ""
        except:
            print("Number expected!")
            print()
            newRating = ""

    myPlayers.editPlayerRating(whichPlayer,int(newRating))
    print()
    print("New rating:", whichPlayer, int(newRating))
    print()
    Pause = input("Hit enter to continue => ")
    while Pause != "":
        Pause = input("INVALID: Hit enter to continue => ")


def changePlayerRecord(whichPlayer, myPlayers):
    print()
    print("Old record:", myPlayers.getWins(whichPlayer), "-", myPlayers.getLosses(whichPlayer))
    print()

    #TRY EXCEPT for input
    newWins = ""
    while newWins == "":
        newWins = input("New wins => ")
        try:
            newWins = int(newWins)
            if newWins < 0:
                print("Can't be negative!")
                newWins = ""
        except:
            print("Number expected!")
            print()
            newWins = ""

    myPlayers.editPlayerWins(whichPlayer, newWins)

    newLosses = ""
    while newLosses == "":
        newLosses = input("New losses => ")
        try:
            newLosses = int(newLosses)
            if newLosses < 0:
                print("Can't be negative!")
                newLosses = ""
        except:
            print("Number expected!")
            print()
            newLosses = ""

    myPlayers.editPlayerLosses(whichPlayer, newLosses)
    print()
    print("New record:", myPlayers.getWins(whichPlayer), "-", myPlayers.getLosses(whichPlayer))
    print()
    Pause = input("Hit enter to continue => ")
    while Pause != "":
        Pause = input("Hit enter to continue => ")


def changePlayerWksPlayed(whichPlayer, myPlayers):
    print()
    print("Old weeks played:", myPlayers.getWksPlayed(whichPlayer))
    print()

    #TRY EXCEPT for input
    newWksPlayed = ""
    while newWksPlayed == "":
        newWksPlayed = input("New weeks played => ")
        try:
            newWksPlayed = int(newWksPlayed)
            if newWksPlayed < 0:
                print("Can't be negative!")
                newWksPlayed = ""
        except:
            print("Number expected!")
            print()
            newWksPlayed = ""

    myPlayers.editWksPlayed(whichPlayer, newWksPlayed)
    print()
    print("New weeks played:", myPlayers.getWksPlayed(whichPlayer))
    print()
    Pause = input("Hit enter to continue => ")
    while Pause != "":
        Pause = input("Hit enter to continue => ")


def showFinishedPlayer(whichPlayer, myPlayers):
    print()
    print("Finished player:")
    print("%-20s %-8d %d %s %-5d %d %-15s" % (whichPlayer, int(myPlayers.getRating(whichPlayer)), int(myPlayers.getWins(whichPlayer)), "-", int(myPlayers.getLosses(whichPlayer)), int(myPlayers.getWksPlayed(whichPlayer)), "wks played"))
    print()
    Pause = input("Hit enter to continue => ")
    while Pause != "":
        Pause = input("Hit enter to continue => ")


def addPlayers(myPlayers):
    Continue = "y"
    while Continue == "y":
        #TRY EXCEPT for input
        whichPlayer = ""
        while whichPlayer == "":
            whichPlayer = input("Name? => ")
            try:
                whichPlayer = int(whichPlayer)
                print("Name expected!")
                print()
                whichPlayer = ""
            except:
                whichPlayer = whichPlayer

        #TRY EXCEPT for input
        Rating = ""
        while Rating == "" or int(Rating) < 0:
            Rating = input("Rating => ")
            try:
                Rating = int(Rating)
                if Rating < 0:
                    print("Can't be negative!")
                    Rating = ""
            except:
                print("Number expected!")
                print()
                Rating = ""


        myPlayers.addPlayer(whichPlayer, int(Rating), 0, 0, 0)
        print()
        print("Player added:", whichPlayer, "   ", int(Rating), "   ", myPlayers.getWins(whichPlayer), "-", myPlayers.getLosses(whichPlayer), "    ", myPlayers.getWksPlayed(whichPlayer), "weeks played    ", myPlayers.getStatus(whichPlayer))
        print()

        #TRY EXCEPT for input
        Continue = ""
        while Continue == "" or Continue not in ['y','n']:
            Continue = input("Add more? (y/n) => ")
            try:
                Continue = int(Continue)
                print("Letter expected!")
                print()
                Continue = ""
            except:
                Continue = Continue


def changePlayerStatus(myPlayers):
    keepGoing = "y"
    while keepGoing == "y":
        print()
        print("ALL players:")
        myPlayers.showAllPlayers()

        #TRY EXCEPT for input
        whichPlayer = ""
        while whichPlayer == "":
            whichPlayer = input("Which player would you like to change? => ")
            try:
                whichPlayer = int(whichPlayer)
                print("Name expected!")
                print()
                whichPlayer = ""
            except:
                if not myPlayers.playerIn(whichPlayer):
                    print("Player not in database")
                    print()
                    whichPlayer = ""
                else:
                    whichPlayer = whichPlayer

        myPlayers.changeStatus(whichPlayer)
        print()
        print("Status changed:")
        print(whichPlayer, "   ", myPlayers.getRating(whichPlayer), "   ", myPlayers.getStatus(whichPlayer))
        print()

        #TRY EXCEPT for input
        keepGoing = ""
        while keepGoing == "" or keepGoing not in ['y','n']:
            keepGoing = input("Change more players? (y/n) => ")
            try:
                keepGoing = int(keepGoing)
                print("Letter expected!")
                print()
                keepGoing = ""
            except:
                keepGoing = keepGoing

    if keepGoing == "n":
        secondAnswer = "n"
    print()
    print()
    print()
    print()
        
def main():
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    print("RATINGS EDIT")
    print()
    myPlayers = playerDatabase()
    answer = "n"
    while answer == "n": #ends on line 820
        print("-------MAIN MENU-------")
        print("1) Upload ratings database")
        print("2) Create new")
        print("3) Close")
        print("-----------------------")

        answer = ""
        while answer == "" or int(answer) < 1 or int(answer) > 3:
            answer = input("Select an option => ")
            try:
                answer = int(answer)
            except:
                print("Number expected!")
                print()
                answer = ""
        if answer == 1: #ends on line 779
            print()

            #TRY EXCEPT for input
            uploadFileName = ""
            while uploadFileName == "":
                uploadFileName = input("File name => ")
                try:
                    myPlayers.uploadDatabase(uploadFileName)
                except:
                    print("Couldn't find file!")
                    print()
                    uploadFileName = ""
            myPlayers.uploadDatabase(uploadFileName)
            
                
            secondAnswer = 'n'
            while secondAnswer == "n": #ends on line 779
                #displays database menu options
                showDatabaseMenu(myPlayers)

                secondAnswer = ""
                while secondAnswer == "" or int(secondAnswer) < 1 or int(secondAnswer) > 9:
                    secondAnswer = input("Select an option => ")
                    try:
                        secondAnswer = int(secondAnswer)
                    except:
                        print("Number expected!")
                        print()
                        secondAnswer = ""
                if secondAnswer == 1: #ends on line 727
                    more = "y"
                    while more == "y": #ends on line 725
                        whichPlayer = ""
                        while whichPlayer == "":
                            whichPlayer = input("Which player? => ")
                            try:
                                whichPlayer = int(whichPlayer)
                                print("Name expected!")
                                print()
                                whichPlayer = ""
                            except:
                                whichPlayer = whichPlayer
                        print()
                        playerIn = myPlayers.playerIn(whichPlayer)
                        if not playerIn:
                            print()
                            addPlayer = ""
                            while addPlayer == "":
                                addPlayer = input("Player not found. Add to database? (y/n) => ")
                                try:
                                    addPlayer = int(addPlayer)
                                    print("Name expected!")
                                    print()
                                    addPlayer = ""
                                except:
                                    addPlayer = addPlayer
                            if addPlayer == "y":
                                print()
                                rating = ""
                                while rating == "":
                                    rating = input("Rating? => ")
                                    try:
                                        rating = int(rating)
                                    except:
                                        print("Number expected!")
                                        print()
                                        rating = ""
                                myPlayers.addPlayer(whichPlayer,int(rating))
                                print("Player added:", whichPlayer, "     ", int(rating))
                            else:
                                print()
                                secondAnswer = 'n'
                                break

                        else:
                            keepGoing = ""
                            while keepGoing != 'no':
                                print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                                print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                                print()
                                print("Editing for:", whichPlayer)
                                print("------PLAYER MENU------")
                                print("1) Change player name")
                                print("2) Edit stats")
                                print("3) Calculate rating change")
                                print("4) FINISH editing player")
                                print("-----------------------")

                                thisAnswer = ""
                                #TRY EXCEPT for input
                                while thisAnswer == "" or int(thisAnswer) < 1 or int(thisAnswer) > 4:
                                    thisAnswer = input("Select an option => ")
                                    try:
                                        thisAnswer = int(thisAnswer)
                                    except:
                                        print("Number expected!")
                                        print()
                                        thisAnswer = ""
                                if thisAnswer == 1:
                                    changePlayerKey(whichPlayer, myPlayers)

                                elif thisAnswer == 2:
                                    displayEditPlayerStatsMenu()

                                    selection = ""
                                    while selection == "" or int(selection) < 1 or int(selection) > 4:
                                        selection = input("Select an option => ")
                                        try:
                                            selection = int(selection)
                                        except:
                                            print("Number expected!")
                                            print()
                                            selection = ""
                                    
                                    if selection == 1:        
                                        changePlayerRating(whichPlayer, myPlayers)

                                    elif selection == 2:
                                        changePlayerRecord(whichPlayer, myPlayers)

                                    elif selection == 3:
                                        changePlayerWksPlayed(whichPlayer, myPlayers)
                                        
                                    else:
                                        pass
                                    keepGoing = ""
                                            
                                elif thisAnswer == 3:
                                    editPlayerStats(myPlayers, whichPlayer)
                                    keepGoing = ""

                                else:
                                    showFinishedPlayer(whichPlayer, myPlayers)
                                    keepGoing = 'no'
                                    
                            print()
                            secondAnswer = "n"
                            more = 'stop'
                    print()
                    print()
                    print()
                    print()

                elif secondAnswer == 2:
                    #adds players to database
                    addPlayers(myPlayers)
                    secondAnswer = 'n'

                elif secondAnswer == 3:
                    #change active/inactive status of players
                    changePlayerStatus(myPlayers)
                    secondAnswer = 'n'

                elif secondAnswer == 4:
                    #goes through all players with for loop and updates stats
                    editAllPlayersStats(myPlayers)
                    secondAnswer = 'n'

                elif secondAnswer == 5:
                    #resets record and wks played of opened database players
                    myPlayers.newSessionStats()
                    print()
                    print("All players RESET:")
                    myPlayers.showAllPlayers()
                    print()
                    secondAnswer = 'n'

                elif secondAnswer == 6:
                    #saves file under original name
                    myPlayers.saveDatabase(uploadFileName)
                    secondAnswer = "y"
                    answer = 'n'
                    print("Saved to:", uploadFileName, ".txt")

                elif secondAnswer == 7:
                    #saves file under new name
                    newFileName = input("New file name => ")
                    myPlayers.saveDatabase(newFileName)
                    print("Saved to:", newFileName, ".txt")
                    secondAnswer = 'y'
                    answer = 'n'

                elif secondAnswer == 8: 
                    newFileName = input("New file name (Will be displayed at top of sheet) => ")

                    #saves original file for keeping sake
                    myPlayers.saveDatabase(uploadFileName)
                    sortedPlayerList = myPlayers.sortPlayers()

                    #saves file under new name and formats for printing
                    myPlayers.saveForPrinting(newFileName, sortedPlayerList)
                    print("Saved to:", newFileName, ".txt")
                    secondAnswer = "y"
                    answer = 'n'
                else:
                    secondAnswer = 'y'
                    answer = 'n'
        elif answer == 2:
            Continue = "y"
            while Continue == "y":
                print()
                print("ADD PLAYERS")
                continueVar = addPlayers(myPlayers)

                if continueVar == "y":
                    Continue = 'y'
                else:
                    Continue = 'n'
                        
            print()
            print("Completed Database:")
            myPlayers.showActivePlayers()

            #TRY EXCEPT for input
            save = ""
            while save == "" or save not in ['y','n']:
                save = input("Save? (y/n) ")
                try:
                    save = int(save)
                    print("Letter expected!")
                    print()
                    save = ""
                except:
                    save = save
                    
            if save == "y":
                fileName = input("File name => ")
                myPlayers.saveDatabase(fileName)
            elif save == 'n':
                myPlayers.clearDatabase()
                print()
                print("DATABASE DELETED")
                answer = 'n'
        else:
            answer = 'y'

        print()

    print("FINISHED EDITING")

main()




