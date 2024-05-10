from tkinter import *
from tkinter import ttk
root = Tk()
root.title("My tkinter App")
root.geometry("240x210")
#root.resizable(0,0)
style = ttk.Style()
style.theme_use('clam')

field_text=""

def btnclick(number):
	global field_text
	field_text = field_text + str(number)
	ans.delete(0,END)
	ans.insert(0,field_text)

def equal():
	global field_text
	result=str(eval(field_text))
	ans.delete(0,END)
	ans.insert(0,result)

def clear():
	global field_text
	ans.delete(0,END)
	field_text = ""

def dlt():
	global field_text
	lngth = len(ans.get())
	ans.delete(first=lngth-1,last=lngth)
	field_text = ans.get()


#title section
title = Label(root,text="Calculator")
ans = Entry(root,text="0")

#buttons
one = Button(root, text="1", fg="black", command=lambda:btnclick(1))
two = Button(root, text="2", fg="black", command=lambda:btnclick(2))
three = Button(root, text="3", fg="black",command=lambda:btnclick(3))
four = Button(root, text="4", fg="black",command=lambda:btnclick(4))
five = Button(root, text="5", fg="black",command=lambda:btnclick(5))
six = Button(root, text="6", fg="black",command=lambda:btnclick(6))
seven = Button(root, text="7", fg="black",command=lambda:btnclick(7))
eight = Button(root, text="8", fg="black",command=lambda:btnclick(8))
nine = Button(root, text="9", fg="black",command=lambda:btnclick(9))
zero = Button(root, text="0", fg="black",command=lambda:btnclick(0))
plus = Button(root, text="+", fg="black",command=lambda:btnclick("+"))
minus = Button(root, text="-", fg="black",command=lambda:btnclick("-"))
multi = Button(root, text="*", fg="black",command=lambda:btnclick("*"))
divis = Button(root, text="/", fg="black",command=lambda:btnclick("/"))
point = Button(root, text=".", fg="black",command=lambda:btnclick("."))
eql = Button(root, text="=", fg="black",command=equal)
delete = Button(root, text="Del", fg="black", command=dlt)
ce = Button(root, text="CE", fg="black",command=clear)

#title grid layout
title.grid(row=1,column=1,columnspan=5)
ans.grid(row=2,column=1,columnspan=5)

#button grid layout 
one.grid(row=3,column=1)
two.grid(row=4,column=1)
three.grid(row=5,column=1)
four.grid(row=3,column=2)
five.grid(row=4,column=2)
six.grid(row=5,column=2)
seven.grid(row=3,column=3)
eight.grid(row=4,column=3)
nine.grid(row=5,column=3)
zero.grid(row=6,column=1)
plus.grid(row=3,column=4)
minus.grid(row=4,column=4)
multi.grid(row=5,column=4)
divis.grid(row=6,column=4)
point.grid(row=6,column=2,columnspan=2)
point.config(width=6)
eql.grid(row=7,column=1,columnspan=2)
eql.config(width=6)
delete.grid(row=7,column=3,columnspan=3)
delete.config(width=10)
ce.grid(row=3,column=5,rowspan=4)
ce.config(height=7)

mainloop()