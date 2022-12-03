def format(fileName):
    fileIn = open(fileName, "r")
    list = []
    keysList = fileIn.readline().strip().split("\t")
    for line in fileIn: # create dictionary out of line
        dictionary = {}
        line = line.strip().split("\t")
        for index in range(0, len(keysList)):
            key = keysList[index]
            dictionary[key] = line[index]
        list.append(dictionary)
    fileIn.close()
    return list


def groupByPlayer(data):
    listPlayers = [] # list of player names
    for row in data:
        if row['Name'] not in listPlayers:
            listPlayers.append(row['Name'])
    dictPlayers = {} # dict holding all the playerRound lists (key=name)
    for player in listPlayers:
        playerRounds = [] # list holding all the row dictionaries that player played
        for row in data:
            if row["Name"] == player:
                playerRounds.append(row)
        dictPlayers[player] = playerRounds
    return dictPlayers


def calcRatios(playerGames):
    names = playerGames.keys()
    ratiosDict = {}
    for name in names:
        ratiosList = []
        roundList = playerGames[name]
        for round in roundList:
            prizesLeft = [] # list containing prizes still in play
            winningPrizesLeft = [] # list containing prizes with more money than the bank offer (called "large outcomes") in the paper
            sum = 0 # sum of remaining prizes (representative value in Ratio RP3)
            keysList = round.keys()
            for key in keysList:
                if round[key] == "1" and key != "Stop Round" and key != "ROUND":
                    # convert to float
                    key = float(key.replace(",", ""))
                    bankOffer = float(round["Bank Offer"].replace(",", ""))
                    sum += key # add sum
                    # append to prize lists
                    prizesLeft.append(key)
                    if key > bankOffer:
                        winningPrizesLeft.append(key)
            ratio = bankOffer / (sum * (len(winningPrizesLeft) / len(prizesLeft)))
            ratiosList.append(ratio)
        ratiosDict[name] = ratiosList
    return ratiosDict


def printRatios(roundRatios):
    for name in roundRatios.keys():
        for ratio in roundRatios[name]:
            print(ratio)


def printAvgRatios(roundRatios):
    for name in roundRatios.keys():
        sumRatios = 0
        for ratio in roundRatios[name]:
            sumRatios += ratio
        print(name, sumRatios/(len(roundRatios[name])))


def main():
    playerGames = groupByPlayer(format("dond_data_with_briefcases.txt")) # dictionary with key=player, value=list of dictionaries of rows, each row representing 1 round
    printAvgRatios(calcRatios(playerGames))
    # to paste into excel sheet:
    printRatios(calcRatios(playerGames))


main()
