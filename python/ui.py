import string
import os

def multiopt(question,opts):
    """
    Gets keyboard input from the user and returns the value they entered.\n
    WARNING! This function only outputs numbers and doesn't allow letters.
    """
    print("\033[1;33m"+question+"\n")
    count = 1
    for x in opts:
        print("  "+str(count)+") "+ str(x))
        count = count + 1
    alphabet = list(string.ascii_letters)
    print("\033[32m")
    inp = input()
    if len(inp) != 1:
        print("\033[1;31m"+inp+" is not a valid input.")
        return Exception