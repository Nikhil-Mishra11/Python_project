import tkinter as tk
import random
from tkinter import DISABLED

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

guesses = 3
secNum = random.choice(numbers)
print(secNum)
won = False
guess = " "

window = tk.Tk()
window.title("Number Guessing Game")

lblInfo = tk.Label(window, text="Guess a number from 0 to 9").pack()
lblLine0 = tk.Label(window, text="________________________________________________________________").pack()
lblNoGuesses = tk.Label(window, text="Max Guesses: 3").pack()
lblLine1 = tk.Label(window, text="________________________________________________________________").pack()
lblMsg = tk.Label(window, text="").pack()

def inpchkguess():
    global guesses, secNum, won, guess
    guess = txtGuess.get(1.0, "end-1c")

    if guesses > 0:
        guesses -= 1
        print(guesses)
        lblNoGuesses.config(text=str(guesses) + " guesses left")
        if guess == secNum:
            won = True
            lblMsg.config(text="You are right! Congratulations!", fg="green")
            txtGuess.config(state=DISABLED)
            chkBtn.config(state=DISABLED)
        elif guess > secNum:
            lblMsg.config(text="Your guess is greater than the number.", fg="red")
        elif guess < secNum:
            lblMsg.config(text="Your guess is lower than the number", fg="red")
        else:
            lblMsg.config(text="Enter a valid number", fg="red")
    else:
        lblNoGuesses.config(text="You have run out of guesses", fg="red")
        txtGuess.config(state=DISABLED)
        chkBtn.config(state=DISABLED)

txtGuess = tk.Text(window, height=1, width=20)
txtGuess.pack()

chkBtn = tk.Button(window, text="Check", command=inpchkguess)
chkBtn.pack()

lblMsg = tk.Label(window, text="")
lblMsg.pack()

lblNoGuesses = tk.Label(window, text="")
lblNoGuesses.pack()

window.mainloop()