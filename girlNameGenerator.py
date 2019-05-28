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
               print(name + " is a possibility")
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



print(possGirlNames(nameList))




