'''
This program calculates r(RP3) according to tab-separated data from "dond_data_with_briefcase.txt"
and finds individual averages for r.

see Chen and John 2021 (Decision Heuristics and Descriptive Choice Models for Sequential
High-Stakes Risky Choices in the Deal or No Deal Game).
In their Ratio-RP3 model, r = banker's offer/(sum of briefcases * proportion of cases greater than banker's offer)
r is used as a measure for an individual's risk tolerance.

'''

# converts entire sheet into a list of rows,
# each row being a dictionary,
# each name being attached to rounds,
# each round being a list of the variables
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


def calcRatios(playerGames): # creates roundRatios
    names = playerGames.keys()
    ratiosDict = {}
    for name in names:
        ratiosList = []
        roundList = playerGames[name]
        # len(playerGames[name]) <- number of rounds played
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
    return ratiosDict #roundRatios


def printRatios(roundRatios):
    for name in roundRatios.keys():
        for ratio in roundRatios[name]:
            print(ratio)


def getDemogInfo(playerGames): # create dictionaries with player demographic info
    list = []
    for player in playerGames.keys():
        dict = {}
        dict["Name"] = player
        for attribute in ["Amount Won", "Deal / No Deal", "Education", "Gender", "Age"]:
            dict[attribute] = playerGames[player][len(playerGames[player])-1][attribute]
        list.append(dict)
    return list

def printAvgRatiosInTxt(roundRatios, demogInfoList):
    fileWrite = open("ratioData.txt", "w")
    # print(roundRatios)
    print("Name\tAvg Ratio\tMax Ratio\tFinal Ratio\tConsistent(Final Ratio = Max Ratio)\tAmount Won\tRounds Played\tDeal / No Deal\tEducation\tGender\tAge", file=fileWrite)
    index = 0
    for name in roundRatios.keys(): # roundRatios.keys() is a list of names
        # do this for every player:
        sumRatios = 0 # keep track of sum to find average later
        maxRatio = 0 # highest attained ratio
        # print(name + "'s ratios:")
        for ratio in roundRatios[name]: # looping through the ratios of each round of one player
            # print(ratio)
            if ratio > maxRatio: # if this is the biggest ratio seen yet
                maxRatio = ratio # set it as the new maxRatio
            sumRatios += ratio
            finalRatio = ratio
        if finalRatio == maxRatio:
            consistent = True
        else:
            consistent = False
        # print all data about them + roundRatios
        print(name + "\t" + str(sumRatios/(len(roundRatios[name]))) + "\t" + str(maxRatio) + "\t" + str(finalRatio) + "\t" + str(consistent) + "\t" + demogInfoList[index]["Amount Won"] + "\t" + str(len(roundRatios[name])) + "\t" + demogInfoList[index]["Deal / No Deal"] + "\t" + demogInfoList[index]["Education"] + "\t" + demogInfoList[index]["Gender"] + "\t" + demogInfoList[index]["Age"], file=fileWrite)
        index += 1

def main():
    playerGames = groupByPlayer(format("dond_data_with_briefcases.txt")) # dictionary with key=player, value=list of dictionaries of rows, each row representing 1 round
    print(playerGames)
    printAvgRatiosInTxt(calcRatios(playerGames), getDemogInfo(playerGames))

main()
