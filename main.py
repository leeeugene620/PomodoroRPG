from tkinter import *
from tkinter.ttk import *

# creates a Tk() object
master = Tk()
master.wm_title("Pomodoro RPG")

# sets the geometry of main
master.geometry("720x480")

main_frame = Frame(master)
shop_frame = Frame(master)
start_frame = Frame(master)


# function to open a new window
# on a button click
def openNewWindow():
    # Toplevel object which will
    # be treated as a new window
    newWin = Toplevel(master)

    # sets the title of the
    # Toplevel widget
    newWin.title("Session Selection")

    # sets the geometry of toplevel
    newWin.geometry("400x200")

    # A Label widget to show in toplevel
    topbut = Button(newWin, text="EASY MODE: 25 minutes of studying and 5 minutes of rest", command=lambda:[toMainScreen(), quit(newWin)])
    topbut.pack(pady=10)
    midbut = Button(newWin, text="NORMAL MODE: 45 minutes of studying and 10 minutes of rest",command=lambda:[toMainScreen(), quit(newWin)])
    midbut.pack(pady=10)
    botbut = Button(newWin, text="HARD MODE: 60 minutes of studying and 20 minutes of rest", command=lambda:[toMainScreen(), quit(newWin)])
    botbut.pack(pady=10)

def toMainScreen():
    mainScreen()

def changeToMain():
   main_frame.pack()
   start_frame.forget()

def quit(self):
    self.destroy()

def openShop():
    # Toplevel object which will
    # be treated as a new window
    newWin = Toplevel(master)

    # sets the title of the
    # Toplevel widget
    newWin.title("Shop")

    # sets the geometry of toplevel
    newWin.geometry("400x200")

    bottomFrame = Frame(newWin)
    bottomFrame.pack(side=BOTTOM)
    # A Label widget to show in toplevel
    topbut = Button(bottomFrame, text="Hat", command=lambda: [chooseTime("top"), quit(newWin)])
    topbut.pack(pady=10)
    midbut = Button(bottomFrame, text="Sword", command=lambda: [chooseTime("mid"), quit(newWin)])
    midbut.pack(pady=10)
    botbut = Button(bottomFrame, text="Shield", command=lambda: [chooseTime("bot"), quit(newWin)])
    botbut.pack(pady=10)


def mainScreen():
    # Toplevel object which will
    # be treated as a new window
    newWin = Toplevel(master)

    # sets the title of the
    # Toplevel widget
    newWin.title("Main")

    # sets the geometry of toplevel
    newWin.geometry("400x200")

    bottomLeftFrame = Frame(newWin)
    bottomLeftFrame.pack(side=BOTTOM, anchor=W)
    bottomRightFrame = Frame(newWin)
    bottomRightFrame.pack(side=BOTTOM, anchor=E)
    topRightFrame = Frame(newWin)
    topRightFrame.pack(side=TOP, anchor=E)
    # A Label widget to show in toplevel
    topbut = Button(topRightFrame, text="Shop" , command=lambda: [chooseTime("top"), quit(newWin)])
    topbut.pack(pady=10)
    midbut = Button(bottomRightFrame, text="Start", command=lambda: [chooseTime("mid"), quit(newWin)])
    midbut.pack(pady=10)
    botbut = Button(bottomLeftFrame, text="Stop", command=lambda: [chooseTime("bot"), quit(newWin)])
    botbut.pack(pady=10)


label = Label(master,
              text="This is the main window")

label.pack(pady=10)

# a button widget which will open a
# new window on button click
btn = Button(master,
             text="Click to begin!",
             command=openNewWindow)
btn.pack(pady=10)

shopbtn = Button(shop_frame, text="Shop", command=openShop)



# mainloop, runs infinitely
mainloop()
