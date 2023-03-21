b0 = 0.195
b1 = 0.991
b2 = -0.057
b3 = -0.037

predictedBOs = []
diffs = []
with open("dond_data_with_boreg", "r+") as f_in:
    keysList = f_in.readline().strip().split("\t")
    roundList = []  # list, each item in list = round, each round = dict called round_info
    for line in f_in:
        round_info = {}  # saves round's bo, ev, cv, nrc as k/v pairs
        newLine = line.split("\t") # round's col values now stored in list
        if newLine[0] != "": # if line isn't blank
            log10EV = float((newLine[keysList.index("log10EV")].strip()))
            cv = float(newLine[keysList.index("CV")].strip())
            nrc = float(newLine[keysList.index("NRC")].strip())
            predictedlog10BO = b0 + b1*log10EV + b2*cv + b3*nrc
            pred_bo = pow(10, predictedlog10BO)
            predictedBOs.append(pred_bo)
            bo = float(newLine[keysList.index("Bank Offer")].replace(",", ""))
            diffs.append(bo-pred_bo)
with open("predicted_bo", "w") as f_out:
    print("Predicted BO\tDifference", file=f_out)
    for i in range(len(predictedBOs)):
        print(str(predictedBOs[i]) + "\t" + str(diffs[i]), file=f_out)