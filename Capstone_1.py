from tkinter import *
from PIL import Image, ImageTk
root = Tk()

def redir(gmid):
	exec(open(str(gmid)+".py").read())

def homepage():
	global img1,img2,img3,clr_img

	img1=ImageTk.PhotoImage(Image.open('python race.png'))
	img2=ImageTk.PhotoImage(Image.open('python race.png'))
	img3=ImageTk.PhotoImage(Image.open('python race.png'))

	clr_img = Button(root, image=img1, command=lambda:redir("Color_Game"))
	clr_txt = Label(root, text="Color Game")
	snk_img = Button(root, image=img2, command=lambda:redir("tictactoe"))
	snk_txt = Label(root, text="Snake Game")
	ttt_img = Button(root, image=img3, command=lambda:redir("test"))
	ttt_txt = Label(root, text="Rock Paper Scissors Game")

	clr_img.pack()
	clr_txt.pack()
	snk_img.pack()
	snk_txt.pack()
	ttt_img.pack()
	ttt_txt.pack()


homepage()

mainloop()
