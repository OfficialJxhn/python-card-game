import random as r
import mysql.connector
import time
from tkinter import *
from tkinter import messagebox
from tkinter.font import Font
#FRONT-END
#BACK-END
#username = john password = test_123
def login_screen():
    login_window = Tk()
    login_window.title("Login")
    login_window.geometry("250x150")
    label1 = Label(login_window,text = "Name: ")
    label1.grid(row = 0, column = 0, sticky="E")

    label2 = Label(login_window,text = "Password: ")
    label2.grid(row = 1, column = 0, sticky="E")

    user_login = Entry(login_window)
    user_login.grid(row = 0, column = 1)

    pass_login = Entry(login_window,show = "*")
    pass_login.grid(row = 1, column = 1)
    enter_button = Button(login_window,text="login", command=lambda: authentication(user_login, pass_login,login_window))
    enter_button.grid(columnspan=2)
    login_window.mainloop()
    return user_login, pass_login,login_window

def authentication(user_login, pass_login,login_window):
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
        login_window.destroy()
    else:
        messagebox.showerror("Login failed", "Incorrect username or password, please try again.")

def draw_cards():
    try:
        global p1_card, p2_card
        p1_card = [i for i in deck[0]]
        deck.pop(0)
        p2_card = [i for i in deck[0]]
        deck.pop(0)
        cards_drawn.config(text=f"Player 1 drew {p1_card} and player 2 drew {p2_card}")
        compare_cards(p1_card, p2_card)
    except IndexError:
        messagebox.showerror("Error","There are no more cards")
        
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
    next_round()
    display_score()

def decide_winner():
        global game_ended
        display_score()
        if p1_card_total > p2_card_total:
            messagebox.showinfo("player 1 wins!!",
                f"""player 1 wins with {p1_card_total} cards
                  here are the winning cards: 
                  {p1_winning_cards}
                  """)
            winner = p1_card_total
        elif p1_card_total < p2_card_total:
            messagebox.showinfo("player 2 wins",
                f"""
                  player 2 wins with {p2_card_total} cards
                  here are the winning cards:
                  {p2_winning_cards}
                  """)
            winner = p2_card_total
        else:
            messagebox.showinfo("It's a tie!")
            game_ended = True
            winner = p1_card_total
        score_board.destroy()
        window_to_ask_for_name(winner)
            
        
def next_round():
    global game_ended
    if len(deck) == 0 and not game_ended:
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
    main_menu_window = Tk()
    main_menu_window.title("Main Menu")
    main_menu_window.geometry("500x500")
    myfont = Font(family="Segoe UI Black",size=12,weight="bold")
    welcome_tag = Label(main_menu_window,text = "Welcome to the game",font=myfont,fg="light blue")
    welcome_tag.pack()
    play_button = Button(main_menu_window,text = "Draw Cards", command= draw_cards)
    play_button.pack()
    leaderboard_button = Button(main_menu_window,text="Leaderboard", command=leaderboard)
    leaderboard_button.pack()
    rules_button = Button(main_menu_window,text= "How to play", command=rules_section)
    rules_button.pack()
    quit_button = Button(main_menu_window,text="Quit", command=quit)
    quit_button.pack()
    main_menu_window.update()

def display_score():
    p1_score_label.config(text=p1_card_total)
    p2_score_label.config(text=p2_card_total)
    score_board.update()

def next_round():
    global game_ended
    if len(deck) == 0 and not game_ended:
        decide_winner()

def window_to_ask_for_name(winner):
    name_window = Tk()
    name_window.geometry("300x100")
    ask_name = Label(name_window,text="Enter your name to be added to the leaderboard (MAX LETTERS 5)")
    enter_name = Entry(name_window)
    ask_name.pack()
    enter_name.pack()
    def add_to_leaderboard():
        name = enter_name.get()
        length = len(name)
        if length <= 5:
            update_leaderboard(winner,name)
            name_window.destroy()
        elif length > 5 or length == 0:
            messagebox.showerror("Error","Name over the limit, please try again")
        
    name_button = Button(name_window,text="Add to leaderboard",command=add_to_leaderboard)
    name_button.pack()
    name_window.mainloop()
    
def update_leaderboard(winner,name):
    file = open("Leaderboard.csv","a")
    file.write(f"{name},{winner}\n")
    file.close()
    
def leaderboard():
    import csv
    x = 1
    leaderboard_window = Tk()
    with open("Leaderboard.csv", "r") as file:
        reader = csv.reader(file)
        next(reader)  # skip header row
        sorted_data = sorted(reader, key=lambda row: int(row[1]), reverse=True)
    
    listbox = Listbox(leaderboard_window)
    listbox.insert(0,"Pos Name Score")
    for index, data in enumerate(sorted_data[:5]):
        listbox.insert(x,f"{index+1} {data[0]} {data[1]}")
        x = x + 1
    listbox.pack()
    leaderboard_window.mainloop()


#main program
game_ended = False
p1_card_total = 0
p2_card_total = 0
#score board in main program
score_board = Tk()
score_board.geometry("300x200")
score_board.title("Current Score")
p1_title = Label(score_board,text="player 1 score")
p1_score_label = Label(score_board,text=p1_card_total)
p2_title = Label(score_board,text="player 2 score")
p2_score_label = Label(score_board,text=p2_card_total)
cards_drawn = Label(score_board,text="")
p1_title.pack()
p1_score_label.pack()
p2_title.pack()
p2_score_label.pack()
cards_drawn.pack()

p1_winning_cards = []
p2_winning_cards = []
colours = ["red", "yellow", "black"]
numbers = range(1, 11)
deck = [(colour, number) for colour in colours for number in numbers]
r.shuffle(deck)
login_screen()