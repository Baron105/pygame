# rock paper scissors in tkinter

from tkinter import *
from tkinter import ttk
from random import randint

class RPS:
    def __init__(self, master):
        self.master = master
        master.title("RPS")
        master.geometry("200x200")
        master.resizable(False, False)

        self.instructions = Label(master, text="Rock, Paper, Scissors!\nSelect one of the following:")
        self.instructions.pack()
        self.label_text = StringVar()
        self.label_text.set("Choose your weapon!")
        self.label = Label(master, textvariable=self.label_text)
        self.label.pack()

        self.rock_button = ttk.Button(master, text="Rock", command=lambda: self.play("Rock"))
        self.rock_button.pack()

        self.paper_button = ttk.Button(master, text="Paper", command=lambda: self.play("Paper"))
        self.paper_button.pack()

        self.scissors_button = ttk.Button(master, text="Scissors", command=lambda: self.play("Scissors"))
        self.scissors_button.pack()

        self.close_button = ttk.Button(master, text="Close", command=master.quit)
        self.close_button.pack()

    def play(self, player_choice):
        choices = ["Rock", "Paper", "Scissors"]
        computer_choice = choices[randint(0,2)]

        if player_choice == computer_choice:
            self.label_text.set("Tie!")
        elif player_choice == "Rock":
            if computer_choice == "Paper":
                self.label_text.set("You lose! {0} covers {1}".format(computer_choice, player_choice))
            else:
                self.label_text.set("You win! {0} smashes {1}".format(player_choice, computer_choice))
        elif player_choice == "Paper":
            if computer_choice == "Scissors":
                self.label_text.set("You lose! {0} cut {1}".format(computer_choice, player_choice))
            else:
                self.label_text.set("You win! {0} covers {1}".format(player_choice, computer_choice))
        elif player_choice == "Scissors":
            if computer_choice == "Rock":
                self.label_text.set("You lose! {0} smashes {1}".format(computer_choice, player_choice))
            else:
                self.label_text.set("You win! {0} cut {1}".format(player_choice, computer_choice))
                
root = Tk()
my_gui = RPS(root)
root.mainloop()