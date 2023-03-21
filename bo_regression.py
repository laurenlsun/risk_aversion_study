import math
import statistics

# log10(BO) = 0.195+0.991log10(EV)-0.057(CV)-0.037NRC
# CV = SD/EV

with open("dond_data_with_sum", "r") as f_in:
    keysList = f_in.readline().strip().split("\t")
    roundList = []  # list, each item in list = round, each round = dict called round_info
    for line in f_in:
        round_info = {}  # saves round's bo, ev, cv, nrc as k/v pairs
        newLine = line.split("\t") # round's col values now stored in list
        if newLine[0] != "": # if line isn't blank
            # print(newLine)
            # remove comma, convert bo to float:
            bo = float(newLine[keysList.index("Bank Offer")].replace(",", ""))

            # get ev
            rc = []  # list of remaining cases
            sum = 0
            nrc = 0 # number of remaining cases
            round = newLine[keysList.index("ROUND")]
            for i in range(10, len(newLine)-1):
                if newLine[i] == "1":
                    case = float(keysList[i].replace(",", ""))
                    sum += case
                    rc.append(case)
            nrc = len(rc)
            ev = (float(sum)/nrc)

            # other vars
            sd = statistics.pstdev(rc)
            cv = sd/ev
            round_info["CV"] = cv
            round_info["NRC"] = nrc
            round_info["log10EV"] = math.log(ev, 10)
            if bo != 0:  # one specific case
                round_info["log10BO"] = math.log(bo, 10)
            else:
                round_info["log10BO"] = 0

            roundList.append(round_info)  # add this rounddict to list of rounddicts

with open("bo_regression.txt", "w") as f_out:
    print("log10BO\tlog10EV\tCV\tNRC", file=f_out)
    for round in roundList:
        print(str(round["log10BO"]) + "\t" + str(round["log10EV"]) + "\t" + str(round["CV"]) + "\t" + str(round["NRC"]), file=f_out)
print(roundList)