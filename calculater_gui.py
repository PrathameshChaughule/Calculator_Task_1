import tkinter as tk 
from tkinter import *

root=tk.Tk()
root.title("Calculater")
root.geometry("570x600+100+200")
root.resizable(False,False)
root.configure(bg="#17161b")

equation = ""

def show(value):
	global equation
	equation+=value
	label_top.config(text=equation)
	
def clear():
	global equation
	equation = ""
	label_top.config(text=equation)
	
def calculate():
	global equation
	result =""
	if equation !="":
		try:
			result= eval(equation)
		except:
			result="error"
			equation=""
	label_top.config(text=result)

label_top= Label(root,width=25,height=2,text="",font=("arial",30))
label_top.pack()

button_c=Button(root,text="C", width=5, height=1,font=("arial",30,"bold"), bd=4, fg="#fff", bg="#3697f5",command=lambda: clear())
button_c.place(x=10,y=100)
button_div=Button(root,text="/", width=5, height=1,font=("arial",30,"bold"), bd=4, fg="#fff", bg="#2a2d36",command=lambda: show("/"))
button_div.place(x=150,y=100)
button_rim=Button(root,text="%", width=5, height=1,font=("arial",30,"bold"), bd=4, fg="#fff", bg="#2a2d36",command=lambda: show("%"))
button_rim.place(x=290,y=100)
button_mul=Button(root,text="*", width=5, height=1, font=("arial",30,"bold"),bd=4, fg="#fff", bg="#2a2d36",command=lambda: show("*"))
button_mul.place(x=430,y=100)

button_7=Button(root,text="7", width=5, height=1,font=("arial",30,"bold"), bd=4, fg="#fff", bg="#2a2d36",command=lambda: show("7"))
button_7.place(x=10,y=200)
button_8=Button(root,text="8", width=5, height=1,font=("arial",30,"bold"), bd=4, fg="#fff", bg="#2a2d36",command=lambda: show("8"))
button_8.place(x=150,y=200)
button_9=Button(root,text="9", width=5, height=1, font=("arial",30,"bold"),bd=4, fg="#fff", bg="#2a2d36",command=lambda: show("9"))
button_9.place(x=290,y=200)
button_sub=Button(root,text="-", width=5, height=1,font=("arial",30,"bold"), bd=4, fg="#fff", bg="#2a2d36",command=lambda: show("-"))
button_sub.place(x=430,y=200)

button_4=Button(root,text="4", width=5, height=1,font=("arial",30,"bold"), bd=4, fg="#fff", bg="#2a2d36",command=lambda: show("4"))
button_4.place(x=10,y=300)
button_5=Button(root,text="5", width=5, height=1,font=("arial",30,"bold"), bd=4, fg="#fff", bg="#2a2d36",command=lambda: show("5"))
button_5.place(x=150,y=300)
button_6=Button(root,text="6", width=5, height=1,font=("arial",30,"bold"), bd=4, fg="#fff", bg="#2a2d36",command=lambda: show("6"))
button_6.place(x=290,y=300)
button_add=Button(root,text="+", width=5, height=1,font=("arial",30,"bold"), bd=4, fg="#fff", bg="#2a2d36",command=lambda: show("+"))
button_add.place(x=430,y=300)

button_1=Button(root,text="1", width=5, height=1,font=("arial",30,"bold"), bd=4, fg="#fff", bg="#2a2d36",command=lambda: show("1"))
button_1.place(x=10,y=400)
button_2=Button(root,text="2", width=5, height=1,font=("arial",30,"bold"), bd=4, fg="#fff", bg="#2a2d36",command=lambda: show("2"))
button_2.place(x=150,y=400)
button_3=Button(root,text="3", width=5, height=1,font=("arial",30,"bold"), bd=4, fg="#fff", bg="#2a2d36",command=lambda: show("3"))
button_3.place(x=290,y=400)

button_div=Button(root,text="/", width=5, height=1,font=("arial",30,"bold"), bd=4, fg="#fff", bg="#2a2d36",command=lambda: show("/"))
button_div.place(x=10,y=500)
button_0=Button(root,text="0", width=5, height=1,font=("arial",30,"bold"), bd=4, fg="#fff", bg="#2a2d36",command=lambda: show("0"))
button_0.place(x=150,y=500)

button_dec=Button(root,text=".", width=5, height=1,font=("arial",30,"bold"), bd=4, fg="#fff", bg="#2a2d36",command=lambda: show("."))
button_dec.place(x=290,y=500)
button_equal=Button(root,text="=", width=5, height=3, font=("arial",30,"bold"), bd=6, fg="#fff", bg="#fe9037",command=lambda: calculate())
button_equal.place(x=430,y=400)

root.mainloop()
