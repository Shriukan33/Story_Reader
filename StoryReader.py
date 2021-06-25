from story import pages
import string
import time as tm
import random as rd
import sys
import os

alphabet = string.ascii_lowercase

def valid_input(text, choices):
    valid_choices = [letter for letter in alphabet[:choices]]
    print(text)
    answer = input().lower().strip() # removes whitespaces
    if answer in valid_choices:
        return answer
    else:
        print("Invalid input, please try again.\n")
        return valid_input(text, choices)

def print1by1(text, lineDelay=0.35, delay=0.025):
    for c in text:
        sys.stdout.write(c)
        sys.stdout.flush()
        tm.sleep(delay)
    tm.sleep(lineDelay) 

def read(page_number):
    page_number = str(page_number)
    print1by1(pages[page_number]["text"], *pages[page_number]["settings"])
    return page_number, len(pages[page_number]["outcomes"])

def set_outcome(current_page, outcomes):
    """
    Each page has a set of outcomes in form of a list which contains the page numbers possible to reach.
    Example : 
        Page 1 has two choices, A and B, leading respectively to page 3 and 4. 
        set_outcome(1, 2) ##  1 = Page number //  2 = number of possible outcomes
        will return 0 if you answer A, and 1 if you answer B. 
        This number will be then used to say what page number the read() function will read among the possible outcomes
    """
    if len(pages[current_page]["outcomes"]) > 1: # If there is only one choice on this page, it  automatically returns the only choice. 
        while True:
            choice = input().lower().strip()
            valid_choices = [letter for letter in alphabet[:outcomes]]
            if choice in valid_choices:
                return valid_choices.index(choice)
            else:
                print("Invalid answer, please try again !")
    else:
        return 0

# Reading start
current_page, outcomes = read("intro") # This is the entry point of the story

while True: # The code will run until it reaches the outcome "exit"

    answer = set_outcome(current_page, outcomes) 
    current_page, outcomes = read(pages[current_page]["outcomes"][answer])
    if pages[current_page]["outcomes"][answer] == "exit":
        break
