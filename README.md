# risk_aversion_study


## ratiorp3

This program is part of a study to investigate differences in risk aversion with respect to different education levels, gender, and age using data from the popular gameshow Deal or No Deal (DOND). The dataset used is from Post et al. (2008) (Deal or No Deal? Decision Making under Risk in a Large-Payoff Game Show). The input is a text file of tab-separated values copied from an excel sheet, which is available  [here](https://www.aeaweb.org/articles?id=10.1257/aer.98.1.38/).

Using one of 36 models described in Chen and John (2021) (Decision Heuristics and Descriptive Choice Models for Sequential High-Stakes Risky Choices in the Deal or No Deal Game), this program calculates r(RP3) and finds individual averages for r.

In their Ratio-RP3 model, r<sub>i</sub> = BO<sub>i</sub>/(sum<sub>i</sub> * pi+<sub>i</sub>), where, at Round i, BO is the Banker's Offer, sum<sub>i</sub> is the sum of prizes left in play, and pi+<sub>i</sub> is the proportion of remaining prizes that are greater than the banker's offer.

Player's r<sub>i</sub>'s are averaged to represent their individual risk tolerance.

## bo_regression

bo_regression calculates log(expected value), pstdev(expected value)/expected value, and number of remaining cases as predictor variables for the banker's offer. These values are calculated for each Deal or No Deal Round played, stored in "dond_data_with_sum.txt". This was used for a multiple regression to predict the banker's offer.

## bo_reg_comparison

This program calculates the difference between the banker's offer predicted by the US primetime regression coefficients from Chen and John 2018 and the actual banker's offers from Post et al. 2008. 

## duplicateCheck

This program flags duplicate first names, which were messing up the algorithm.
