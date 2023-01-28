'''
This program takes a list of names in names.txt and flags duplicates of names
that do not follow immediately after one another. The list of names is taken from
the player column in the DOND dataset. Ensuring that no name is repeated prevents
issues in calculating the RP3 ratio later.
'''
file = open("names.txt", "r") # open file
newName = "m" # set file name to anything
names = [] # list containing all previous names
for line in file:
    if line != newName:
        newName = line
        print(newName, end="")
        if newName not in names:
            names.append(newName)
        else:
            print("DUPLICATE:", newName)