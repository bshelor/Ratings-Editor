#Class for people with one value associated with each person (ratings)
class playerDatabase:
    def __init__(self):
        self.players = {}
        #{Bryson Shelor: [865, 12, 5, 3, 'Active']}

    def addPlayer(self, name, rating, wins, losses, wksPlayed):
        self.players[name] = []
        self.players[name].append(int(rating))
        self.players[name].append(int(wins))
        self.players[name].append(int(losses))
        self.players[name].append(int(wksPlayed))
        self.players[name].append("Active")

    def clearDatabase(self):
        self.players = {}

    def playerIn(self,name):
        playerIn = False
        for player in self.players:
            if player == name:
                playerIn = True
        if not playerIn:
            return False
        else:
            return True

    def newSessionStats(self):
        for player in self.players:
            self.players[player][1] = 0
            self.players[player][2] = 0
            self.players[player][3] = 0

    def changePlayerKey(self, oldName, newName):
        self.players[newName] = self.players.pop(oldName)

    def showActivePlayers(self):
        for name in self.players:
            if self.players[name][4] == "Active":
                print("%-20s %-8d %d %s %-5d %d %-15s" % (name, int(self.players[name][0]), int(self.players[name][1]), "-", int(self.players[name][2]), int(self.players[name][3]), "wks played"))
##                print(ljust(20,name), "    ", self.players[name][0], "    ", self.players[name][1], "-", self.players[name][2], "   ", self.players[name][3], "wks played")

    def showAllPlayers(self):
        for name in self.players:
##            print(ljust(20,name), "    ", int(self.players[name][0]), "   ", self.players[name][1], "-", self.players[name][2], "   ", self.players[name][3], "wks played    ", self.players[name][4])
            print("%-20s %-8d %d %s %-5d %d %-15s %-5s" % (name, int(self.players[name][0]), int(self.players[name][1]), "-", int(self.players[name][2]), int(self.players[name][3]), "wks played", self.players[name][4]))

    def changeStatus(self, player):
        for name in self.players:
            if name == player:
                if self.players[player][4] == "Active":
                    self.players[player][4] = "Inactive"
                else:
                    self.players[player][4] = "Active"

    def getListOfActivePlayers(self):
        playerList = []
        for player in self.players:
            if self.players[player][4] == 'Active':
                playerList.append(player)
        return playerList

    def editPlayerRating(self,name,newRating):
        self.players[name][0] = newRating

    def editPlayerWins(self, name, newWins):
        self.players[name][1] = newWins

    def editPlayerLosses(self, name, newLosses):
        self.players[name][2] = newLosses

    def editWksPlayed(self, name, newWksPlayed):
        self.players[name][3] = newWksPlayed

    def addWins(self, name, numAdd):
        return int(self.players[name][1]) + numAdd

    def addLosses(self, name, numAdd):
        return int(self.players[name][2]) + numAdd

    def addWksPlayed(self, name, numAdd):
        return int(self.players[name][3]) + numAdd
        
    def getRating(self,name):
        return int(self.players[name][0])

    def getWins(self, name):
        return int(self.players[name][1])

    def getLosses(self, name):
        return int(self.players[name][2])

    def getWksPlayed(self, name):
        return int(self.players[name][3])

    def getStatus(self,name):
        return self.players[name][4]

    def uploadDatabase(self, fileName):
        fileName += ".txt"
        inFile = open(fileName,"r")
        for line in inFile:
            if line[-1] == "\n":
                newLine = line[:-1]
                objects = list(newLine.split(","))
                for item in range(len(objects)):
                    if item == 0:
                        name = objects[item]
                        self.players[name] = []
                    else:
                        self.players[name].append(objects[item])
            else:
                objects = list(line.split(","))
                for item in range(len(objects)):
                    if item == 0:
                        name = objects[item]
                        self.players[name] = []
                    else:
                        self.players[name].append(objects[item])
        inFile.close()

    def sortPlayers(self):
        sortedPlayerList = []
        for player in self.players:
            if self.players[player][4] == "Active":
                if len(sortedPlayerList) > 0:
                    for name in range(len(sortedPlayerList)):
                        if player not in sortedPlayerList:
                            if int(self.players[player][0]) > int(self.players[sortedPlayerList[name]][0]):
                                sortedPlayerList.insert(name, player)
                            elif int(self.players[player][0]) == int(self.players[sortedPlayerList[name]][0]):
                                if ord(player[0]) <= ord(sortedPlayerList[name][0]):
                                    sortedPlayerList.insert(name, player)
                                else:
                                    if name == len(sortedPlayerList) - 1:
                                        sortedPlayerList.append(player)
                                    else:
                                        sortedPlayerList.insert(name + 1, player)
                            elif name == len(sortedPlayerList) - 1:
                                sortedPlayerList.append(player)
                else:
                    sortedPlayerList.append(player)
        return sortedPlayerList

    def saveForPrinting(self, fileName, sortedPlayerList):
        fileName += ".txt"
        outFile = open(fileName, "w")
        outFile.write("%-5s %-20s %-8s %-10s %-15s" % ("Rank", "Name", "Rating", "Record", "Weeks Played"))
        outFile.write("\n")
        for name in range(1,len(sortedPlayerList) + 1):
            if name != len(sortedPlayerList):
                if int(self.players[sortedPlayerList[name - 1]][0]) == int(self.players[sortedPlayerList[name]][0]):
                    outFile.write("%-5d %-20s %-8d %-2d %-2s %-8d %-15d" % (name, sortedPlayerList[name - 1], int(self.players[sortedPlayerList[name - 1]][0]), int(self.players[sortedPlayerList[name - 1]][1]), "-", int(self.players[sortedPlayerList[name - 1]][2]), int(self.players[sortedPlayerList[name - 1]][3])))
                    outFile.write("\n")
                    outFile.write("%-5d %-20s %-8d %-2d %-2s %-8d %-15d" % (name, sortedPlayerList[name], int(self.players[sortedPlayerList[name]][0]), int(self.players[sortedPlayerList[name]][1]), "-", int(self.players[sortedPlayerList[name]][2]), int(self.players[sortedPlayerList[name]][3]))) 
                    outFile.write("\n")
                elif int(self.players[sortedPlayerList[name - 1]][0]) == int(self.players[sortedPlayerList[name - 2]][0]):
                    pass
                else:
                    outFile.write("%-5d %-20s %-8d %-2d %-2s %-8d %-15d" % (name, sortedPlayerList[name - 1], int(self.players[sortedPlayerList[name - 1]][0]), int(self.players[sortedPlayerList[name - 1]][1]), "-", int(self.players[sortedPlayerList[name - 1]][2]), int(self.players[sortedPlayerList[name - 1]][3])))
                    outFile.write("\n")
            else:
                if int(self.players[sortedPlayerList[name - 1]][0]) == int(self.players[sortedPlayerList[name - 2]][0]):
                    outFile.write("%-5d %-20s %-8d %-2d %-2s %-8d %-15d" % (name - 1, sortedPlayerList[name - 1], int(self.players[sortedPlayerList[name - 1]][0]), int(self.players[sortedPlayerList[name - 1]][1]), "-", int(self.players[sortedPlayerList[name - 1]][2]), int(self.players[sortedPlayerList[name - 1]][3])))
                    outFile.write("\n")
                else:
                    outFile.write("%-5d %-20s %-8d %-2d %-2s %-8d %-15d" % (name, sortedPlayerList[name - 1], int(self.players[sortedPlayerList[name - 1]][0]), int(self.players[sortedPlayerList[name - 1]][1]), "-", int(self.players[sortedPlayerList[name - 1]][2]), int(self.players[sortedPlayerList[name - 1]][3])))
   
        outFile.close()
                                                                                                                                                           
            
                          

    def saveDatabase(self,fileName):
        fileName += ".txt"
        outFile = open(fileName, "w")
        for name in self.players:
            outFile.write(name)
            outFile.write(",")
            for times in range(5):
                if times == 4:
                    outFile.write(str(self.players[name][times]))
                else:
                    outFile.write(str(self.players[name][times]))
                    outFile.write(",")
            outFile.write("\n")
        outFile.close()

##    def removePlayer(self,name):

##myPlayers = playerDatabase()
##myPlayers.addPlayer("Bob Turner", 1200, 0, 0, 0)
##myPlayers.addPlayer("Jim", 1200, 12, 2, 3)
##myPlayers.addPlayer("joe", 435, 5, 12, 4)
##myPlayers.addPlayer("Dave", 1201, 4, 12, 0)
##myPlayers.addPlayer("Alex", 435, 3, 15, 0)
##myPlayers.saveDatabase("players")
##myPlayers.uploadDatabase("players")
##myPlayers.showAllPlayers()
##myPlayers.addWins("Bob Turner", 5)
##print()
##myPlayers.showAllPlayers()
##sortedPlayerList = myPlayers.sortPlayers()
##myPlayers.saveForPrinting("playersPrint", sortedPlayerList)


        

