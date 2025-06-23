from tkinter import *
import pygame
import time
import random

root = Tk()
root.title("scientificoders")
root.geometry("1000x500")
root.configure(background="black")

balance = 1000

def main():
    Current_balance_main = Label(root,text=f"Your current balance is :- ${balance}",bg="black",fg="yellow")
    Balance_tuple = ("Arial",25)
    Current_balance_main.configure(font=Balance_tuple)
    Current_balance_main.grid(row=0,column=0,padx=0,pady=10,rowspan=2,columnspan=8)

    Welcome = Label(root,text="The Casino Game",bg="black",fg="yellow")
    Welcome_tuple = ("Arial",60,"bold")
    Welcome.configure(font= Welcome_tuple)
    Welcome.grid(row=2,column=1,rowspan=2,columnspan=30,padx=150)

    #BUTTONS

    guess_btn = Button(root,text="Guess",background="light blue",height=1,width=5,bd=10)
    guess_tuple = ("Arial",40,"bold")
    guess_btn.configure(font=guess_tuple)
    guess_btn.grid(row=4,column=6,columnspan=1,padx=150)


def destroy_call_guess():
    e_choose.destroy()
    Choose.destroy()
    Congratulations.destroy()
    num_label.destroy()
    Current_balance_guess1.destroy()
    Play_again_btn.destroy()
    Current_balance_guess.destroy()
    Back_Btn.destroy()
    Try.destroy()
    Bet.destroy()
    e.destroy()
    Start_Btn.destroy()
    Start_Btn1.destroy()
    GUESS()

def destroy_call_main():
    e_choose.destroy()
    Choose.destroy()
    Congratulations.destroy()
    num_label.destroy()
    Current_balance_guess1.destroy()
    Play_again_btn.destroy()
    Current_balance_guess.destroy()
    Back_Btn.destroy()
    Try.destroy()
    Bet.destroy()
    e.destroy()
    Start_Btn.destroy()
    Start_Btn1.destroy()
    main()



def bet_choosed():
    global balance,Congratulations,Current_balance_guess1,num_label,Play_again_btn
    try:
        choosen_num = int(e_choose.get())
    except ValueError:
        choosen_num = 0

    num_list = [1,2,3,4,5]
    num = random.choice(num_list)
    num_label = Label(root,text=f"Computer choosed :- {num}",background="black",foreground="light blue")
    num_tuple = ("Arial",45,"bold")
    num_label.configure(font=num_tuple)
    num_label.grid(row=7,column=1,padx=10,pady=10,columnspan=30)
    time.sleep(2)

    if(choosen_num==num):
        Congratulations = Label(root,text=f"CONGO YOU WON :- ${bet_guess*2}",background="black",foreground="orange")
        Congo_Tuple = ("Arial",40,"bold")
        Congratulations.configure(font=Congo_Tuple)
        Congratulations.grid(row=8,column=2,padx=10,pady=10,columnspan=35)
        "pygame".mixer.music.load("Songs/Winning.wav")
        "pygame".mixer.music.play(loops=0)
        Current_balance_guess.destroy()
        balance = balance + bet_guess
        Current_balance_guess1 = Label(root,text=f"Your current balance is :- ${balance}",bg = "black",fg = "yellow")
        Balance_tuple = ("Arial",25)
        Current_balance_guess1.configure(font=Balance_tuple)
        Current_balance_guess1.grid(row=0,column=1,pady=5,rowspan=2,columnspan=5)

    else:
        Congratulations = Label(root,text=f"OOPS ! You Lost :- ${bet_guess}",background="black",foreground="orange")
        Congo_Tuple = ("Arial",40,"bold")
        Congratulations.configure(font=Congo_Tuple)
        Congratulations.grid(row=8,column=2,padx=10,pady=10,columnspan=35)
        "pygame".mixer.music.load("Songs/Lost.wav")
        "pygame".mixer.music.play(loops=0)
        Current_balance_guess.destroy()
        balance = balance - bet_guess
        Current_balance_guess1 = Label(root,text=f"Your current balance is :- ${balance}",bg = "black",fg = "yellow")
        Balance_tuple = ("Arial",25)
        Current_balance_guess1.configure(font=Balance_tuple)
        Current_balance_guess1.grid(row=0,column=1,pady=5,rowspan=2,columnspan=5)
    
    Play_tuple = ("Arial",20,"bold")
    Play_again_btn = Button(root,text="Play Again",background="blue", foreground="light blue",font=Play_tuple,command=destroy_call_guess)
    Play_again_btn.grid(row=9,column=3,columnspan=10,padx=10)


def bet_try_guess():

    global e_choose,bet_guess,Choose,Start_Btn

    try:
        bet_guess = int(e.get())
    except ValueError:
        bet_guess = 100

    if(bet_guess<=balance):
        Choose = Label(root,text="Choose a number b/w [1-5] :-         ",bg="black",fg="green")
        Choose_Tuple = ("Arial",20,"bold")
        Choose.configure(font=Choose_Tuple)
        Choose.grid(row=6,column=1,pady=5,columnspan=10)

        e_choose = Entry(root,width=10,bg="light blue",fg="blue")
        e_choose.grid(row=6,column=6,pady=5,columnspan=5)

        Start_Tuple = ("Arial",10,"bold")

        Start_Btn = Button(root,text="Done",background="yellow",foreground="red",font= Start_Tuple,command=bet_choosed)
        Start_Btn.grid(column=12,row=6,columnspan=5)


def GUESS():

    global Current_balance_guess,e,Bet,Back_Btn,Try,Start_Btn1,balance

    "rules_btn".destroy()
    "guess_btn".destroy()
    "seven_btn".destroy()
    "Welcome".destroy()
    "Current_balance_main".destroy()
    "roulette_btn".destroy()

    Back_Btn = Button(root,text="Back",background="yellow",foreground="red",bd=5,height=1,width=4,command=destroy_call_main)
    Back_Tuple = ("Arial",15)
    Back_Btn.configure(font=Back_Tuple)
    Back_Btn.grid(row=0,column=0,padx=10,pady=10)

    Current_balance_guess = Label(root,text=f"Your current balance is :- ${balance}",bg="black",fg="yellow")
    Balance_tuple = ("Arial",25)
    Current_balance_guess.configure(font=Balance_tuple)
    Current_balance_guess.grid(row=0,column=1,padx=0,pady=5,rowspan=2,columnspan=5)

    Try = Label(root,text="Let's Try Your Luck !!",bg="black",fg="yellow")
    Try_Tuple = ("Arial",50,"bold")
    Try.configure(font=Try_Tuple)
    Try.grid(row=3,column=1,padx=60,pady=5,columnspan=30,rowspan=2)

    Bet = Label(root,text="Place Your Bet :-- ",bg="black",fg="green")
    Bet_tuple = ("Arial",20,"bold")
    Bet.configure(font=Bet_tuple)
    Bet.grid(row=5,column=1,pady=5,columnspan=10)

    e = Entry(root,width=20,bg="light blue",fg="blue")
    e.grid(row=5,column=5,pady=5,columnspan=10)

    Start_Tuple = ("Arial",10,"bold")
    Start_Btn1 = Button(root,text="Place",background="yellow",foreground="red",font=Start_Tuple,bd=3,command=bet_try_guess)
    Start_Btn1.grid(column=12,row=5,columnspan=5)


main()
root.mainloop()


from tkinter import *
import time
# yimport random
from random import randint
money = int(100)

# main_screen = Tk()
# main_screen.title('Horse Racing')
# main_screen.geometry('600*500')
# main_screen.config(background='white')

play = input("Do you want to play a game of High/Low? Y or N?")
print("for the first time we have credited 100 dollars in your account")
while play.lower()=="y":
    number = randint(1,10)
    
    
    guess = input("Guess H for high or L for low.")
    if guess.lower()=="h":
        if number > 5:
            print("YOu guessed correctly! The number was", number)
            money = money + 10
            print("You have", money, "dollars.")
            play = input("play gain? Y or N?")
            if money < 1:
                print("You have run out of money, time to go to the ATM.")
                print("Your money has been reset.")
                money = int(100)
                
        if number < 6:
            print("You guessed wrong! The number was", number)
            money = money - 10
            print("You havw", money, "dollars.")
            play = input("play gain? Y or N?")
            if money < 1:
                print("You have run out of money, time to go to the ATM.")
                print("Your money has been reset.")
                money = int(100)
                    
                    
    if guess.lower()=="l":
        if number < 6:
            print("YOu guessed correctly! The number was", number)
            money = money + 10
            print("You have", money, "dollars.")
            play = input("play gain? Y or N?")
            if money < 1:
                print("You have run out of money, time to go to the ATM.")
                print("Your money has been reset.")
                money = int(100)
                
        if number > 5:
            print("You guessed wrong! The number was", number)
            money = money - 10
            print("You havw", money, "dollars.")
            play = input("play gain? Y or N?")
            if money < 1:
                print("You have run out of money, time to go to the ATM.")
                print("Your money has been reset.")
                money = int(100)
    
    if play.lower()=="n":
        print()
        print("Okay, The game is over.")
        print("You Finished with", money, "dollars")
        
# main_screen.mainloop()
