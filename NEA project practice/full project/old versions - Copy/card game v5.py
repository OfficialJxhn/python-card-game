import random as r
import mysql.connector
import time
from tkinter import *
from tkinter import messagebox
#username = john password = test_123
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
        main_menu()
        login_screen.quit()
    else:
        messagebox.showerror("Login failed", "Incorrect username or password, please try again.")

def draw_cards():
    p1_card = [i for i in deck[0]]
    deck.pop(0)
    p2_card = [i for i in deck[0]]
    deck.pop(0)
    compare_cards(p1_card, p2_card)
    decide_winner()

def compare_cards(p1_card, p2_card):
    global p1_card_total, p2_card_total
    if (p1_card[0] == p2_card[0]) and (p1_card[1] == p2_card[1]):
        print("its a draw")
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
    display_score()
    score_board.mainloop()
    next_round()

def decide_winner():
        global game_ended
        if p1_card_total > p2_card_total:
            print(f"""
                  player 1 wins with {p1_card_total} cards
                  here are the winning cards: {p1_winning_cards}
                  """)
            time.sleep(5)
            quit()
        elif p1_card_total < p2_card_total:
            print(f"""
                  player 2 wins with {p2_card_total} cards
                  here are the winning cards: {p2_winning_cards}
                  """)
            time.sleep(5)
            quit()
        else:
            print("It's a tie!")
            game_ended = True
            time.sleep(5)
            quit()

def next_round():
    global game_ended
    if len(deck) <= 0 or not game_ended:
        decide_winner()
        time.sleep(2)  
    else:
        answer = messagebox.askquestion("question", "Start the next round?")
        if answer == "yes":
            draw_cards()
            
        elif answer == "no":
            if not game_ended:
                decide_winner()
                
    
def rules_section():
    from os import startfile
    startfile("rules.txt")
        
    
def main_menu():
    root = Tk()
    root.title("Main Menu")
    root.geometry("500x500")
    welcome_tag = Label(root,text = "Welcome to the game")
    welcome_tag.pack()
    play_button = Button(root,text = "Play game", command= draw_cards)
    play_button.pack()  
    rules_button = Button(root,text= "How to play", command=rules_section)
    rules_button.pack()
    quit_button = Button(root,text="Quit", command=quit)
    quit_button.pack()
    root.mainloop()

def display_score():
    global p1_card_total, p2_card_total, p1_score_label, p2_score_label
    p1_score_label.config(text=p1_card_total)
    p2_score_label.config(text=p2_card_total)

def next_round():
    global game_ended
    if len(deck) == 0 and not game_ended:
        decide_winner()

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

score_board = Tk()
score_board.title("Current Score")
p1_title = Label(score_board, text="player 1 score")
p1_score_label = Label(score_board, text=p1_card_total)
p2_title = Label(score_board, text="player 2 score")
p2_score_label = Label(score_board, text=p2_card_total)
p1_title.pack()
p1_score_label.pack()
p2_title.pack()
p2_score_label.pack()
login_screen()