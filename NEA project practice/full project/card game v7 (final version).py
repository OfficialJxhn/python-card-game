import random as r
import mysql.connector
from tkinter import *
from tkinter import messagebox
from tkinter.font import Font
from PIL import Image,ImageTk

#===========================================================FRONT-END=========================================================================================#
def login_screen():
    #here im using tkinter to create the login screen 
    login_window = Tk()
    login_window.geometry("253x132")
    login_window.configure(background="#9489f7") #used hexadecimal to get a specific type of purple background
    login_window.title("Login")
    name_label = Label(login_window,text = "Name: ",bg="#9489f7")
    name_label.grid(row = 0, column = 0) #i used rows and columns instead of .pack() as this way it made the login screen look more organised

    password_label = Label(login_window,text = "Password: ",bg="#9489f7")
    password_label.grid(row = 1, column = 0)

    user_login = Entry(login_window)
    user_login.grid(row = 0, column = 1)

    pass_login = Entry(login_window,show = "*")#show is used here because when the user enters their password it will come up with *** instead of the password, makes it look more authentic and secure
    pass_login.grid(row = 1, column = 1)
    enter_button = Button(login_window,text="login", command=lambda: authentication(user_login, pass_login,login_window),bg="#da001c") #the use of lambda here is to create a anonymous function that takes no arguements to then call the function authentication function, this is because in order to use the command option for the button i had to pass a function but for authentication i also need arguements for it therefore using lambda made it so i didnt need to pass arguments
    enter_button.grid(columnspan=3)
    login_window.mainloop()
    return user_login, pass_login,login_window #returns the username and password from the login_window to be used in the authentication function

def decide_winner():
        update_score()
        if p1_card_total > p2_card_total:
            messagebox.showinfo("player 1 wins!!", #i used these notification boxes to show that the game was over and requiring the players to finish the game, it also looked better than just having text in the gui 
                f"player 1 wins with {p1_card_total} cards")
            winner = p1_card_total # winner score is amount of cards the winning player (e.g. player 1) had
        elif p1_card_total < p2_card_total:
            messagebox.showinfo("player 2 wins",
                f"player 2 wins with {p2_card_total} card ")
            winner = p2_card_total
        else:
            messagebox.showinfo("It's a tie!","Its a tie!")
            winner = p1_card_total
        score_board.destroy()#this will close the scoreboard window signifying that the game is over
        window_to_ask_for_name(winner) #this will pass the winners score to the function to be entered into the leaderboard

def rules_section():
    from os import startfile
    startfile("rules.txt") # this will open the notepad app to open the rules.txt file
        
def main_menu():
    main_menu_window = Tk()
    main_menu_window.configure(background="light blue")
    main_menu_window.title("Main Menu")
    main_menu_window.geometry("300x200")
    font_for_game = Font(family="Segoe UI Black",size=12,weight="bold") #this is used for getting the type of font, letter size, and making the letters bold for the title of the window
    welcome_tag = Label(main_menu_window,text = "Welcome to the card game",font=font_for_game,fg="green",bg="light blue")
    welcome_tag.pack()
    play_button = Button(main_menu_window,text = "Draw Cards", command= draw_cards)#when this buttn is pressed, the draw_cards function is called, starting the game
    play_button.pack()
    leaderboard_button = Button(main_menu_window,text="Leaderboard", command=leaderboard)#this is display the leaderboard
    leaderboard_button.pack()
    rules_button = Button(main_menu_window,text= "How to play", command=rules_section)#this will open the rules
    rules_button.pack()
    quit_button = Button(main_menu_window,text="Quit", command=quit)#this will stop the program and close it
    quit_button.pack()
    main_menu_window.update()
    
    def change_colour(): #this function is used to change the colour of the "draw cards" button, making it more appealing and less boring
        colour = "#{0:06x}".format(r.randint(0,256**3-1))#this changes the colour of the button randomly 
        play_button.config(bg=colour)#this will update the colour of the button
        play_button.after(200,change_colour)#thus will change the colour of the button every 200 milliseconds
    change_colour()
    
def update_score():
    p1_score_label.config(text=p1_card_total) #this will show will update the score of the players after each round
    p2_score_label.config(text=p2_card_total)
    score_board.update()

def window_to_ask_for_name(winner):
    name_window = Tk()
    name_window.geometry("600x100")
    name_window.configure(background="white")
    ask_name = Label(name_window,text="Enter your name to be added to the leaderboard (MAX LETTERS 5)",font = font_for_scorelabels,fg="purple",bg="white")
    enter_name = Entry(name_window)
    ask_name.pack()
    enter_name.pack()
    def add_to_leaderboard():#the reason for a function inside the function is because it would reduce the amount of lines needed in this code, also no need to make any variables global or return them
        name = enter_name.get()
        length = len(name)
        if length <= 5:
            update_leaderboard(winner,name)
            name_window.destroy()
        elif length > 5 or length == 0:
            messagebox.showerror("Error","Name is too long, please try again") #error checking which alerts the user that their name is too long and gives them another chance to enter or shorten a names
        
    name_button = Button(name_window,text="Add to leaderboard",command=add_to_leaderboard,fg="purple") # this will call the add_leaderboard
    name_button.pack()
    name_window.mainloop()
    
def update_leaderboard(winner,name): #this function opens the leaderboard.csv file and write the name and score of the winner of the game
    file = open("Leaderboard.csv","a")
    file.write(f"{name},{winner}\n")
    file.close()
    
def leaderboard():
    import csv #this is needed to read the csv file as python cant normally read these
    x = 1
    leaderboard_window = Tk() #creating a seperate window to display the leaderboard
    leaderboard_window.geometry = ("150x100")
    leaderboard_window.title = "Leaderboard"
    with open("Leaderboard.csv", "r") as file:
        reader = csv.reader(file)
        next(reader)  #skips the header row
        sorted_data = sorted(reader, key=lambda row: int(row[1]), reverse=True)#lambda is used here to sort the data in based on their score in descending order as if lambda wasnt used the sorted function will automatically do it in ascending order not based on what on the order of data
    
    listbox = Listbox(leaderboard_window)#creates a list box to display the leaderboard
    listbox.insert(0,"Pos Name Score")
    for index, data in enumerate(sorted_data[:5]):
        listbox.insert(x,f"{index+1} {data[0]} {data[1]}")
        x = x + 1#this is the position of the player in the leaderboard
    listbox.pack()
    leaderboard_window.mainloop()


#===========================================================BACK-END=========================================================================================#
#username = john password = test_123
def authentication(user_login, pass_login,login_window):
    db = mysql.connector.connect( # use of mysql to store usernames and password as i thought it would be better than just using a csv file or txt file
        host="localhost",
        user="root",
        password="root",
        database="store_information" # these are needed for the python program to connect to the mysql database
    )
    mycursor = db.cursor()
    username = user_login.get() #gets username from the login window
    passcode = pass_login.get() #gets password from the login window
    sql_query = "SELECT * FROM info WHERE username = %s AND password = %s" #selects everything from the info table where the username = username entered and the password = password entered
    mycursor.execute(sql_query, (username, passcode)) # executes the query
    result = mycursor.fetchall()
    if result: #if a result is returned from the query then then the user is allowed to login (only one username and pasasword on this whole database)
        messagebox.showinfo("Login successful", f"Welcome back {username}!")
        main_menu() #opens the main menu
        login_window.destroy() #closes the login window
    else:
        messagebox.showerror("Login failed", "Incorrect username or password, please try again.")#if thw username or password are false and there is no match for the username or password then this error message will be displayed

def draw_cards():
    try:
        global p1_card, p2_card
        p1_card = [i for i in deck[0]] # takes the first card from the deck 
        deck.pop(0) # removes the first card from the deck
        p2_card = [i for i in deck[0]] # takes the second card from the deck
        deck.pop(0) # removes the second card from the deck and so on...
        #i found that using a dictionaryhere was better then a using an if-statement as using if-statemnets here made my code ridiculously long and inefficient
        card_images = [ #i used a dictionary here so instead of using a large amount of if-statements to find what card was drawn, the program can just go through the dictionary and compare it with the cards drawn to then output a image of the card drawn
        {"colour": "red", "number": 1, "img": "red 1.png"},
        {"colour": "red", "number": 2, "img": "red 2.png"},
        {"colour": "red", "number": 3, "img": "red 3.png"},
        {"colour": "red", "number": 4, "img": "red 4.png"},
        {"colour": "red", "number": 5, "img": "red 5.png"},
        {"colour": "red", "number": 6, "img": "red 6.png"},
        {"colour": "red", "number": 7, "img": "red 7.png"},
        {"colour": "red", "number": 8, "img": "red 8.png"},
        {"colour": "red", "number": 9, "img": "red 9.png"},
        {"colour": "red", "number": 10, "img": "red 10.png"},
        {"colour": "yellow", "number": 1, "img": "yellow 1.png"},
        {"colour": "yellow", "number": 2, "img": "yellow 2.png"},
        {"colour": "yellow", "number": 3, "img": "yellow 3.png"},
        {"colour": "yellow", "number": 4, "img": "yellow 4.png"},
        {"colour": "yellow", "number": 5, "img": "yellow 5.png"},
        {"colour": "yellow", "number": 6, "img": "yellow 6.png"},
        {"colour": "yellow", "number": 7, "img": "yellow 7.png"},
        {"colour": "yellow", "number": 8, "img": "yellow 8.png"},
        {"colour": "yellow", "number": 9, "img": "yellow 9.png"},
        {"colour": "yellow", "number": 10, "img": "yellow 10.png"},
        {"colour": "black", "number": 1, "img": "black 1.png"},
        {"colour": "black", "number": 2, "img": "black 2.png"},
        {"colour": "black", "number": 3, "img": "black 3.png"},
        {"colour": "black", "number": 4, "img": "black 4.png"},
        {"colour": "black", "number": 5, "img": "black 5.png"},
        {"colour": "black", "number": 6, "img": "black 6.png"},
        {"colour": "black", "number": 7, "img": "black 7.png"},
        {"colour": "black", "number": 8, "img": "black 8.png"},
        {"colour": "black", "number": 9, "img": "black 9.png"},
        {"colour": "black", "number": 10, "img": "black 10.png"},
    ]

        for card in card_images: #loop through the dictionary
            if card["colour"] == p1_card[0] and card["number"] == p1_card[1]: #compares the colour of the card to the colours in the dictionary + the numbers
                p1_pic_card = Image.open(card["img"]) #once the colour and number is found then a image corresponding to the colour and the number will be outputed to the score_board
                photo = ImageTk.PhotoImage(p1_pic_card)
                p1_display_drawn_card.config(image=photo)
                p1_display_drawn_card.image = photo #this is required as without it the images will appear blank
                break
        for card in card_images:
            if card["colour"] == p2_card[0] and card["number"] == p2_card[1]:
                p2_pic_card = Image.open(card["img"])
                photo = ImageTk.PhotoImage(p2_pic_card)
                p2_display_drawn_card.config(image=photo)
                p2_display_drawn_card.image = photo
                break
        cards_drawn.config(text=f"Player 1 drew {p1_card} and player 2 drew {p2_card}")
        compare_cards(p1_card, p2_card)
    except IndexError:#i used a try and except here as a way of error checking as when there are no more cards and the game is finished, the "draw cards" button can still be clicked causing a possible crash
                    #therefore by using try and except and identify the which error occurred i can display and error message stating why theres a error and if they want to play again they would have to restart the program
        messagebox.showerror("Error","There are no more cards, to play again restart the game")

        
def compare_cards(p1_card, p2_card):
    global p1_card_total, p2_card_total 
    if p1_card[0] == p2_card[0]: #if the players have a card of the same colour then the program will compare their numbers 
        if p1_card[1] > p2_card[1]:
            winner_of_round.config(text="👑Player 1 wins!!!👑",font=font_for_scorelabels)
            p1_card_total += 2 #player who wins will gain 2 points 1 for their card and the another for taking the other players card
            p1_winning_cards.append(p1_card) #adds the cards used in this round to this variable
            p1_winning_cards.append(p2_card)
        elif p1_card[1] < p2_card[1]:
            winner_of_round.config(text="👑Player 2 wins!!!👑",font=font_for_scorelabels)
            p2_card_total += 2
            p2_winning_cards.append(p2_card)
            p2_winning_cards.append(p1_card)
    else:
        if (p1_card[0] == "red" and p2_card[0] == "black") or (p1_card[0] == "black" and p2_card[0] == "yellow") or (p1_card[0] == "yellow" and p2_card[0] == "red"): #compares the different colour combinations there are 
            winner_of_round.config(text="👑Player 1 wins!!!👑",font=font_for_scorelabels)
            p1_card_total += 2
            p1_winning_cards.append(p1_card)
            p1_winning_cards.append(p2_card)
        else:
            winner_of_round.config(text="👑Player 2 wins!!!👑",font=font_for_scorelabels)
            p2_card_total += 2
            p2_winning_cards.append(p2_card)
            p2_winning_cards.append(p1_card)
    next_round()#opens the function if the deck is empty 
    update_score() #this opens the function to update the score after each round
                
def next_round():
    if len(deck) == 0: # whden there are no more cards in the deck, game ends and winner is decided in the decide_winner function
        decide_winner()

#main program also back end
#this is here as i needed to make most of variables/windows here global variables as if they werent then the game wouldnt work as well as it currently is, this does however result in the score board being displayed with the login screen 
p1_card_total = 0 # variable of the current score of each player
p2_card_total = 0
#score board in main program
score_board = Tk()
score_board.title("Current Score")
score_board.geometry("500x400")
font_for_scorelabels = Font(family = "Segoe UI Black",size=12,weight="bold")
score_board.configure(background="grey")

p1_title = Label(score_board,text="player 1 score",font=font_for_scorelabels,bg="grey",fg="#ff0001") #shows the title for players score
p1_score_label = Label(score_board,text=p1_card_total,bg="grey",font=font_for_scorelabels,fg="#ff0001") #shows the current score of the players

p2_title = Label(score_board,text="player 2 score",font=font_for_scorelabels,bg="grey",fg="#0000ff")
p2_score_label = Label(score_board,text=p2_card_total,bg="grey",font=font_for_scorelabels,fg="#0000ff")

cards_drawn = Label(score_board,text="",bg="grey",fg="black",font=font_for_scorelabels)
p1_display_drawn_card = Label(bg="grey") #this is where the images of the current drawn cards will be
p2_display_drawn_card = Label(bg="grey")
winner_of_round = Label(bg="grey",fg="orange")

p1_title.pack()
p1_score_label.pack()
p2_title.pack()
p2_score_label.pack()
winner_of_round.pack()
cards_drawn.pack()
p1_display_drawn_card.place(x=100,y=200) #this is the position of where the images of the current drawn cards will be displayed
p2_display_drawn_card.place(x=350,y=200)

p1_winning_cards = [] #list to hold the winning cards of the players  
p2_winning_cards = []
colours = ["red", "yellow", "black"] #list of the differnt colours 
numbers = range(1, 11)#this chooses a random number between 1 and 11
deck = [(colour, number) for colour in colours for number in numbers] #this inputs a tuple into a list with a randomized number and colour 
r.shuffle(deck) # this shuffles the deck
login_screen() # this opens the login screen