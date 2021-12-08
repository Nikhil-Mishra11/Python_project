from tkinter import *
import random
import ast
root = Tk()

root.configure(background="Black")
root.geometry("1650x900")
label = Label(root, text="Welcome to XPERO : A simple gaming management system", fg = "White",font="comicsansms 25 bold ", padx=10,pady=15, background="Black").place(x=250, y=50)

canvas = Canvas(root,width=1458,height=750,highlightthickness=0)
canvas.place(x = 0 , y = 150)
img = PhotoImage(file="new.png")
canvas.create_image(0,0,anchor = NW,image = img)
playerlist={}
with open('players.txt','r') as f:
    playerlist=ast.literal_eval(f.read())
def new(): 
 
    newplayer = Toplevel(root) 
    newplayer.title("Game Window") 
    newplayer.geometry("400x250") 
    newplayer.configure(bg="sky blue") 
    Label(newplayer, bg="sky blue",text="Enter Your Details", font="comicsansms 20 bold", pady=15).grid(row=0,column=0,columnspan=2) 
    
 
    name = Label(newplayer,font="comicsansms 15 bold", bg="sky blue",text="Name") 
    Username = Label(newplayer,font="comicsansms 15 bold",bg="sky blue", text="Username") 
    gender = Label(newplayer,font="comicsansms 15 bold", bg="sky blue",text="Gender") 
     
 
#Pack text for our form 
    name.grid(row=1, column=0) 
    Username.grid(row=2, column=0) 
    gender.grid(row=3, column=0) 
 
 
 
# Tkinter variable for storing entries 
    global namevalue
    global Usernamevalue
    global gendervalue
    namevalue = StringVar() 
    Usernamevalue = StringVar() 
    gendervalue = StringVar() 
     
 
 
#Entries for our form 
    
    nameentry = Entry(newplayer, font="comicsansms 15 bold",textvariable=namevalue) 
    Usernameentry = Entry(newplayer, font="comicsansms 15 bold",textvariable=Usernamevalue) 
    genderentry = Entry(newplayer, font="comicsansms 15 bold",textvariable=gendervalue) 
   
# Packing the Entries

    nameentry.grid(row=1, column=1) 
    Usernameentry.grid(row=2, column=1) 
    genderentry.grid(row=3, column=1) 
     
 
 
     
 
#Button & packing it and assigning it a command 
    Label(newplayer,text='',bg='sky blue').grid(row=4,column=0) 
    Button(newplayer,text="Submit your Details", command=Game,font="comicsansms 10 bold",fg='white',bg='blue').grid(row=5, column=0,columnspan=2)


b1 = Button(
    root,
    text='Click here to register',
    font=('Times', 20),
    padx=10,
    pady=10,
    bg='orange',
    fg='Black',
    activebackground='green',
    activeforeground='white',
    command=new
    )

b1.place(x = 20 , y = 600)


def Game():
    particle = Toplevel(root)
    particle.title("Game Window")
    particle.geometry("1300x800")
    particle.configure(bg="slateBlue1")
   
    Label(particle,text="Select the game you want to play ",font="comicsansms 25 bold ", padx=10,pady=15, background="VioletRed1").place(x = 350,y = 20)
   
    canvas2 = Canvas(particle,width=1600,height=800,highlightthickness=0)
    canvas2.place(x = 0 , y = 100)
    img2 = PhotoImage(file="2396.png")
    particle.img2 = img2
    canvas2.create_image(1,1,anchor = CENTER,image = img2)

    b3 = Button(
    particle,
    text='Snake game',
    font=('Times', 20),
    padx=10,
    pady=10,
    bg='magenta2',
    fg='yellow',
    activebackground='green',
    activeforeground='white',
    command=snakegame
    
    )

    b3.place(x = 10 , y = 200)

    b4 = Button(
    particle,
    text='Ping Pong game',
    font=('Times', 20),
    padx=10,
    pady=10,
    bg='magenta2',
    fg='yellow',
    activebackground='green',
    activeforeground='white',
    command=ping
    )

    b4.place(x = 10, y = 400)

    b5 = Button(
    particle,
    text='Correct guess',
    font=('Times', 20),
    padx=10,
    pady=10,
    bg='magenta2',
    fg='yellow',
    activebackground='green',
    activeforeground='white',
    command=guessgame
    )

    b5.place(x = 10, y = 600)


b2 = Button(
    root,
    text='Continue as a Guest',
    font=('Times', 20),
    padx=10,
    pady=10,
    bg='orange',
    fg='Black',
    activebackground='green',
    activeforeground='white',
    command=Game
    )

b2.place(x = 1200 , y = 600)

def snakegame():
    import newsnake
    if Usernamevalue.get() not in playerlist.keys():
        playerlist[Usernamevalue.get()]=[namevalue.get(),gendervalue.get(),newsnake.score]
    else:
        if(playerlist[Usernamevalue.get()][2]<newsnake.score):
            print("HighScore")
            playerlist[Usernamevalue.get()][2]=newsnake.score
        else:
            print("Not high score")
    with open('players.txt','w') as f:
        f.write(str(playerlist))

def guessgame():
    import guess

def ping():
    import shambhavi


root.mainloop()