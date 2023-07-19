# i imported random function for shuffling the cards
# i imported tkinter for the GUI
import random as r
from tkinter import *
import tkinter as tk

#main shuffling function
def shuffler():
    colours = ["red", "black", "yellow"]
    numbers =  range(1,11)
    create_deck = [(colours, numbers) for colour in colours for number in numbers]
    r.shuffle(create_deck)
    return finding_winner(create_deck)
#function for making each player draw unique cards
def finding_winner(create_deck):
    p1_cards = []
    p2_cards = []
    while len(create_deck) > 0:
        card1 = create_deck.pop(0)
        card2 = create_deck.pop(0)
        actual_game(card1, card2)
        
        winner = actual_game(card1, card2)
        
        if winner == "player 1":
            p1_cards.append([card1, card2])
        elif winner == "player 2":
            p2_cards.append([card1, card2])
        else:
            p1_cards.append([card1, card2])
            p2_cards.append([card1, card2])
        

def actual_game(card1, card2):
    colour1 = card1
    number1 = card1
    colour2 = card2
    number2 = card2
    
    if colour1 == colour2:
        if number1 > number2:
            print(f"player 1 drew {colour1} {number1} and player 2 drew {colour2} {number2} player 1 wins")
            return "player 1"
        elif number1 < number2:
            print(f"player 1 drew {colour1} {number1} and player 2 drew {colour2} {number2} player 2 wins")
            return "player 2"
        else:
            print("Its a tie")
            return "tie"
    else:
        if (colour1 == "red" and colour2 == "black") or (colour1 == "black" and colour2 == "red"):
            print(f"player 1 drew {colour1} {number1} and player 2 drew {colour2} {number2} player 1 wins")
            return "player 1"
            
        elif (colour1 == "black" and colour2 == "yellow") or (colour1 == "yellow" and colour2 == "black"):
            print(f"player 1 drew {colour1} {number1} and player 2 drew {colour2} {number2} player 1 wins")
            return "player 1"
            
        elif (colour1 == "yellow" and colour2 == "red") or (colour1 == "red" and colour2 == "yellow"):
            print(f"player 1 drew {colour1} {number1} and player 2 drew {colour2} {number2} player 2 wins")
            return "player 2"
        else:
            print("Its a tie")
            return "tie"

print(shuffler())