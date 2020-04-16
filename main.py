#Made by dark#9999 on discord
import os
import glob
from termcolor import colored
#from bots.mekpreme import mekpreme
import bots.mekpreme
botList = []
for file in os.listdir("./bots"):
    botList.append(file.replace(".py", ""))
if "__pycache__" in botList:
    botList.remove("__pycache__")

print("/==================================")
print("|  _       ___     __           __ ")
print("| | |     / (_)___/ /___ ____  / /_")
print("| | | /| / / / __  / __ `/ _ \/ __/")
print("| | |/ |/ / / /_/ / /_/ /  __/ /_  ")
print("| |__/|__/_/\__,_/\__, /\___/\__/  ")
print("|                /____/            ")
print("|                                  ")
print("|===============INFO===============")
print("| Developed by    :   dark#9999    ")
print("| Version         :   0.0.1        ")
print("|========CURRENTLY SUPPORTS========")
print("| " + ", ".join(botList))
print("\==================================")

class Main:
    def __init__(self):
        self.jsonPath = None
        self.botOutput = None
        self.botInput = None
    botInput = input("Please input what bot you would like to convert from: ")
    index = 1
    while index == 1:
        if botInput in botList:
            index = 2
            jsonPath = input("Please input the path to the profile JSON. Must be in profileConvert folder: ")
        else:
            botInput = input(colored("Invalid bot. Please try again: ", "red"))
    while index == 2:
        if os.path.isfile(jsonPath):
            index = 3
            botOutput = input("Please input what bot you would like to convert to: ")
        else:
            jsonPath = input(colored("Invalid file. Please try again. **REMEMEBR** Must be in profileConvert folder: ", "red"))
    while index == 3:
        if botInput in botList:
            index = 4
            bots.mekpreme.convert(botOutput, jsonPath)
        elif botInput == botOutput:
            botInput = input(colored("You cannot convert to the same bot. Please try again: ", "red"))
        else:
            botInput = input(colored("Invalid bot. Please try again: ", "red"))

def __main__():
    Main()