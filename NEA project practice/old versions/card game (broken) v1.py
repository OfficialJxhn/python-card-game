# i imported random function for shuffling the cards
# i imported tkinter for the GUI
import random as r
from tkinter import *
import tkinter as tk

red = []
black = []
yellow = []
choice = ["red", "black", "yellow"]

#main shuffling function
def shuffler(colour):
    #this function is used to "shuffle" the red cards
    def shuffle_red():
        while len(red) < 10:
            random_num = r.randint(1, 10)
            if random_num in red:
                continue
            
            red.append(random_num)
        return red

    def shuffle_black():
        while len(black) < 10:
            random_num = r.randint(1, 10)
            if random_num in black:
                continue
            
            black.append(random_num)
        return black

    def shuffle_yellow():
        while len(yellow) < 10:
            random_num = r.randint(1, 10)
            if random_num in yellow:
                continue
            
            yellow.append(random_num)
        return yellow
    
    match colour:
        case "red":
            return shuffle_red()
        case "black":
            return shuffle_black()
        case "yellow":
            return shuffle_yellow()
    return red, black, yellow
#function for making each player draw unique cards
def drawing_cards():
    p1_rand_colour = r.randint(0, 2)
    player1_choice = shuffler(choice[p1_rand_colour])
    p1_rand_num = 0
    player1_card = f"player 1 drew: {(choice[p1_rand_colour])} {player1_choice[p1_rand_num]}"
    
    p2_rand_colour = r.randint(0, 2)
    p2_rand_num = 0
    player2_choice = shuffler(choice[p2_rand_colour])
    player2_card = f"player 2 drew: {(choice[p2_rand_colour])} {player2_choice[p2_rand_num]}"
    return player1_card, player2_card

def compare_cards(player1_card, player2_card):
    #this takes the number on the players cards from the variable
    player1_card_num = int(player1_card.split()[-1])
    player2_card_num = int(player2_card.split()[-1])
    
    #this takes the colour of the players cards from teh variable
    player1_card_colour = player1_card.split()[2]
    player2_card_colour = player2_card.split()[2]
    
    #the holy grail of if statements :)
    if player1_card_colour == "red":
        if player2_card_colour == "black":
            return f"{player1_card} and {player2_card} player 1 wins"
        elif player2_card_colour == "yellow":
             return f"{player1_card} and {player2_card} player 2 wins"
    elif player1_card_colour == "black":
        if player2_card_colour == "yellow":
            return f"{player1_card} and {player2_card} player 1 wins"
        elif player2_card_colour == "red":
            return f"{player1_card} and {player2_card} player 2 wins"
    elif player1_card_colour == "yellow":
        if player2_card_colour == "red":
            return f"{player1_card} and {player2_card} player 1 wins"
        elif player2_card_colour == "black":
            return f"{player1_card} and {player2_card} player 2 wins"
    elif player1_card_colour == player2_card_colour:
        if player2_card_num > player1_card_num:
            return f"{player1_card} and {player2_card} player 2 wins"
        elif player2_card_num < player1_card_num:
            return f"{player1_card} and {player2_card} player 1 wins"
        else:
            return "tie"

def remove_cards(player1_card, player2_card, red, black, yellow):
    # this takes the number on the players cards from the variable
    player1_card_num = int(player1_card.split()[-1])
    player2_card_num = int(player2_card.split()[-1])

    # this takes the colour of the players cards from the variable
    player1_card_colour = player1_card.split()[2]
    player2_card_colour = player2_card.split()[2]

    # remove the drawn card from the respective color list
    if player1_card_colour == "red":
        red.remove(player1_card_num)
    elif player1_card_colour == "black":
        black.remove(player1_card_num)
    elif player1_card_colour == "yellow":
        yellow.remove(player1_card_num)

    if player2_card_colour == "red":
        red.remove(player2_card_num)
    elif player2_card_colour == "black":
        black.remove(player2_card_num)
    elif player2_card_colour == "yellow":
        yellow.remove(player2_card_num)

    return red, black, yellow


    
print(compare_cards(drawing_cards()[0], drawing_cards()[1]))
print("")
print(remove_cards(drawing_cards()[0], drawing_cards()[1],red,black,yellow))
