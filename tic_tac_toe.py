# tic tac toe game in tkinter

from tkinter import *
from tkinter import ttk
from random import randint

class TicTacToe:
    def __init__(self,master):
        self.master = master
        master.title("Tic Tac Toe")
        master.geometry("300x300")
        
        self.instructions = Label(master, text="Tic Tac Toe!\n Put your X's/O's in the grid!")
        self.instructions.pack()
        self.label_text = Label(master, text="Choose your character (X/O):")
        self.label_text.pack()
        
        self.x_button = ttk.Button(master, text="X", command=lambda: self.play("X"))
        self.x_button.pack()
        
        self.o_button = ttk.Button(master, text="O", command=lambda: self.play("O"))
        self.o_button.pack()
        
        self.close_button = ttk.Button(master, text="Close", command=master.quit)
        
        self.grid = [[0,0,0],[0,0,0],[0,0,0]]
        self.turn = 0
        self.game_over = False
        
    def play(self, player_choice):
        if player_choice == "X":
            self.computer_choice = "O"
            self.player_choice = "X"
        else:
            self.computer_choice = "X"
            self.player_choice = "O"
        
        self.label_text.destroy()
        self.x_button.destroy()
        self.o_button.destroy()
        
        self.close_button.pack()
        
        self.game = Frame(self.master)
        self.game.pack()
        
        self.buttons = []
        
        for i in range(3):
            self.buttons.append([])
            for j in range(3):
                self.buttons[i].append(ttk.Button(self.game, text=" ", command=lambda i=i, j=j: self.update(i,j)))
                self.buttons[i][j].grid(row=i, column=j)
                
    def update(self, i, j):
        if self.grid[i][j] == 0 and not self.game_over:
            self.grid[i][j] = self.player_choice
            self.buttons[i][j].configure(text=self.player_choice)
            self.turn += 1
            self.check_win()
            if not self.game_over:
                self.computer_move()
                self.check_win()
                
    def computer_move(self):
        while True:
            i = randint(0,2)
            j = randint(0,2)
            if self.grid[i][j] == 0:
                self.grid[i][j] = self.computer_choice
                self.buttons[i][j].configure(text=self.computer_choice)
                self.turn += 1
                break
            
    def check_win(self):
        for i in range(3):
            if self.grid[i][0] == self.grid[i][1] == self.grid[i][2] != 0:
                self.game_over = True
                if self.label_text:
                    self.label_text.destroy()
                self.label_text = Label(self.master, text="Game over! {0} wins!".format(self.grid[i][0]))
                self.label_text.pack()
                break
            elif self.grid[0][i] == self.grid[1][i] == self.grid[2][i] != 0:
                self.game_over = True
                if self.label_text:
                    self.label_text.destroy()
                self.label_text = Label(self.master, text="Game over! {0} wins!".format(self.grid[0][i]))
                self.label_text.pack()
                break
        if self.grid[0][0] == self.grid[1][1] == self.grid[2][2] != 0:
            self.game_over = True
            if self.label_text:
                self.label_text.destroy()
            self.label_text = Label(self.master, text="Game over! {0} wins!".format(self.grid[0][0]))
            self.label_text.pack()
        elif self.grid[0][2] == self.grid[1][1] == self.grid[2][0] != 0:
            self.game_over = True
            if self.label_text:
                self.label_text.destroy()
            self.label_text = Label(self.master, text="Game over! {0} wins!".format(self.grid[0][2]))
            self.label_text.pack()
        elif self.turn == 9:
            self.game_over = True
            self.label_text = Label(self.master, text="Game over! Tie!")
            self.label_text.pack()
            
root = Tk()
my_gui = TicTacToe(root)
root.mainloop()  