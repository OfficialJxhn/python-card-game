import random as r
import mysql.connector
import time
from tkinter import *
from tkinter import messagebox

def login_screen():
    root = Tk()
    label1 = Label(root,text = "Name: ")
    label1.grid(row = 0, column = 0, sticky="E")

    label2 = Label(root,text = "Password: ")
    label2.grid(row = 1, column = 0, sticky="E")

    user_login = Entry(root)
    user_login.grid(row = 0, column = 1)

    pass_login = Entry(root)
    pass_login.grid(row = 1, column = 1)
    enter_button = Button(root,text="login", command=lambda: authentication(user_login, pass_login))
    enter_button.grid(columnspan=2)
    root.mainloop()
    return user_login, pass_login

def authentication(user_login, pass_login):
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="store_information"
    )
    mycursor = db.cursor()
    username = user_login.get()
    passcode = pass_login.get()
    sql_query = "SELECT * FROM info WHERE username = %s AND password = %s"
    mycursor.execute(sql_query, (username, passcode))
    result = mycursor.fetchall()
    if result:
        messagebox.showinfo("Login successful", f"Welcome back {username}!")
        draw_cards()
    else:
        messagebox.showerror("Login failed", "Incorrect username or password, please try again.")
        
def draw_cards():
    p1_card = [i for i in deck[0]]
    deck.pop(0)
    p2_card = [i for i in deck[0]]
    deck.pop(0)
    compare_cards(p1_card, p2_card)

def compare_cards(p1_card, p2_card):
    global p1_card_total, p2_card_total
    if p1_card[0] == p2_card[0]:
        if p1_card[1] > p2_card[1]:
            print("Player 1 wins!")
            p1_card_total += 2
            p1_winning_cards.append(p1_card)
            p1_winning_cards.append(p2_card)
        else:
            print("Player 2 wins!")
            p2_card_total += 2
            p2_winning_cards.append(p2_card)
            p2_winning_cards.append(p1_card)
    else:
        if (p1_card[0] == "red" and p2_card[0] == "black") or (p1_card[0] == "black" and p2_card[0] == "yellow") or (p1_card[0] == "yellow" and p2_card[0] == "red"):
            print("Player 1 wins!")
            p1_card_total += 2
            p1_winning_cards.append(p1_card)
            p1_winning_cards.append(p2_card)
        else:
            print("Player 2 wins!")
            p2_card_total += 2
            p2_winning_cards.append(p2_card)
            p2_winning_cards.append(p1_card)
    next_round()

def decide_winner():
        global game_ended
        if p1_card_total > p2_card_total:
            print(f"""
                  player 1 wins with {p1_card_total} cards
                  here are the winning cards: {p1_winning_cards}
                  """)
        elif p1_card_total < p2_card_total:
            print(f"""
                  player 2 wins with {p2_card_total} cards
                  here are the winning cards: {p2_winning_cards}
                  """)
        else:
            print("It's a tie!")
            game_ended = True
  

def next_round():
    global game_ended
    if len(deck) == 0 and not game_ended:
        decide_winner()
        time.sleep(2)
        play_again()
        
    else:
        continue_game = input("Would you like to play again? (y/n): ")
        if continue_game == "yes":
            draw_cards()
        elif continue_game == "no":
            if not game_ended:
                decide_winner()
                time.sleep(2)
                play_again()

def play_again():
    start_again = input("Would you like to play again? (y/n): ")
    if start_again == "Y" or "y":
        game_ended = False
        return game_ended
    else:
        print("Thanks for playing")
        
#main program
game_ended = False
p1_card_total = 0
p2_card_total = 0

p1_winning_cards = []
p2_winning_cards = []
colours = ["red", "yellow", "black"]
numbers = range(1, 11)
deck = [(colour, number) for colour in colours for number in numbers]
r.shuffle(deck)
login_screen()