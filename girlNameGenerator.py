# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 02:55:41 2019

@author: Garrett Sloup

GIRL NAME GENERATOR
POSSIBLE GIRL NAMES WITH A MIDDLE CHARACTER OF "D"

Program reads a txt file (girlNamesList.txt) of the 1000 most common baby girl names from:
    https://www.verywellfamily.com/top-1000-baby-girl-names-2757832

Program also has access to 2287 other girl names (longerGirlsNameList.txt).
    Link can no longer be found.


Will go through each name and determine if the name has an odd num of 
characters and the middle character is a "d".

v2)Adds functionality to take the returned list of possible names and will 
    eliminate any duplicate names.
"""


names = ["Maddy", "Sadie", "Addison", "Jade"]

def exampleLogic(names):
   """
   Iterates through a list of names, printing out whether or not
   a particular name is both an odd num of letters and the 
   middle char is a 'd'.
   
   returns NoneType
   """
   for name in names:
       # checks if num letters in name is odd
       if len(name) % 2 == 1:
           # checks if the middle letter is a 'd'
           if name[len(name)//2] == "d":
               print(name + " is a possiblity")
           else:
               print(name + "'s middle letter isn't a 'D'.")
       else:
           print(name + "'s name has even letters.")

#Tests logic used to determine valid name
# UNCOMMENT LINE BELOW TO RUN
#exampleLogic(names)


       
# Word file containing top 1000 girls' names
#WORDFILE = "girlNamesList.txt"

# Word file containing 2287 girls' names
WORDFILE = "longerGirlsNameList.txt"

def loadWords():
    """
    Returns a list of valid baby names. Names are strings.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading girl name list from file...")
    # inFile: file
    inFile = open(WORDFILE, 'r')
    # nameList: list of strings
    namesList = []
    for line in inFile:
        namesList.append(line.strip())
    print("  ", len(namesList), "names loaded.")
    return namesList

nameList = loadWords()


def possGirlNames(nameList):
    """
    Iterates through the nameList, returning a new list of possible
    girl names that are an odd num of characters and the middle
    character is a 'd'.
    
    Expects an array of strings
    """
    possibleNames = []
    for name in nameList:
         # checks if num letters in name is odd
        if len(name) % 2 == 1:
            # checks if the middle letter is a 'd'
            if name[len(name)//2] == "d":
                possibleNames.append(name)
    print("Total possible names: " + str(len(possibleNames)))
    return possibleNames


# List of all viable names including duplicate names
viableNames = possGirlNames(nameList)
print("List of all possible names:")
print(viableNames)


def zipNames(name1, name2):
    """
    Takes 2 different names as arguments
    (i.e. name1 and name2).  Type = String

    Returns a list of tuples, pairing each letter
    in the corresponding names based on their 
    location in the sequence

    ex) name1 = "hi"
        name2 = "HI"
        returns [('h','H'),('i', 'I')]
    """
    pairs = list(zip(name1,name2))
    return pairs

def findDifferences(pairs):
    """
    Iterates through each given tuple pair(arg), 
    tracking the number of different letter pairs. 

    Returns the number(int) of differing letter pairs.
    """
    dif_letters = 0
    for x,y in pairs:
        if x != y:
            dif_letters +=1
    return dif_letters


# Eliminating any duplicate names from the viableNames list
repeat_names = []
# Nested for-loop to compare each name to each other only once.
for a in range(len(viableNames)):
    for b in range(a+1, len(viableNames)):
        # Checks if the name lengths are the same (solves problem with zip() pairing)
        if len(viableNames[a]) == len(viableNames[b]) and \
        viableNames[a][0] == viableNames[b][0]:         # Checks that the first letter of each name is the same
            pairs = zipNames(viableNames[a], viableNames[b])
            totalDiff = findDifferences(pairs)
            # Names will be considered duplicates if totalDiff == 1.
            if totalDiff == 1:
                #print(viableNames[a]+ " vs " + viableNames[b])
                repeat_names.append(viableNames[b])
print("List of duplicate names:")
print(repeat_names)

# viableNames - repeat_names = uniqueNames
uniqueNames = []
for name in viableNames:
    if name not in repeat_names:
        uniqueNames.append(name)
print("List of unique baby girl names:")
print(uniqueNames)