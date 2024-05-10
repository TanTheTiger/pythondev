from tkinter import *
import random
colours = ["Red", "Blue", "Green", "Pink", "Black", "Yellow", "Orange", "White", "Purple", "Brown"]
score = 0
timeleft = 60

def startGame(event):
	if timeleft == 60:
		countdown()
	nextColour()

def nextColour():
	global score
	global timeleft
	if timeleft > 0:
		entry.focus_set()
		if entry.get().lower() == colours[1].lower():
			score += 1
		entry.delete(0, END)
		random.shuffle(colours)
		mnlbl.config(fg = str(colours[1]),text = str(colours[0]))
		scrlbl.config(text = "Score: "+str(score))

def countdown():
	global timeleft
	if timeleft > 0:
		timeleft -= 1
		tmlbl.config(text = "Time left:"+str(timeleft))
		tmlbl.after(1000, countdown)

root = Tk()
root.title("Color Game")
root.geometry("375x200")
instr = Label(root, text = "Type in the colour of the words, and not the word text!")
scrlbl = Label(root, text = "Press enter to start")
tmlbl = Label(root, text = "Time left: "+str(timeleft))
mnlbl = Label(root)
entry = Entry(root)
root.bind("<Return>", startGame)

instr.pack()
scrlbl.pack()
tmlbl.pack()
mnlbl.pack()
entry.pack()
entry.focus_set()
root.mainloop()

#This is a comment