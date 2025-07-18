from tkinter import *
def click(event):
    global scvalue
    text = event.widget.cget("text")
    print(text)
    if text=="=":
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            try:
                value = eval(screen.get())
            except Exception as e:
                value = "Error"
                
        scvalue.set(value)
        screen.update()
    elif text == "c":
        scvalue.set("")
        screen.update()
    else: 
        scvalue.set(scvalue.get() + text)
        screen.update()

window = Tk()
window['bg']="black"
window.geometry("350x550")
window.minsize(250,470)
window.title("Calculator")
scvalue = StringVar()
scvalue.set("")
screen = Entry(window, textvar=scvalue,font="lucida 40 bold")
screen.pack(fill=X, ipadx=8, pady=10, padx=10)

i=9
while i>0:
   
    f1=Frame(window, bg="black")
    b=Button(f1, text=str(i), font="lucida 25 bold",width=4,bg="grey",fg="white")
    b.pack(side=LEFT)
    b.bind("<Button-1>",click)

    b=Button(f1, text=str(i-1), font="lucida 25 bold",width=4,bg="grey",fg="white")
    b.pack(side=LEFT)
    b.bind("<Button-1>",click)

    b=Button(f1, text=str(i-2), font="lucida 25 bold",width=4,bg="grey",fg="white")
    b.pack(side=LEFT)
    b.bind("<Button-1>",click)

    f1.pack()
    i=i-3

f1=Frame(window, bg="black")
b=Button(f1, text="0", font="lucida 25 bold",width=4,bg="grey",fg="white")
b.pack(side=LEFT)
b.bind("<Button-1>",click)

b=Button(f1, text="00", font="lucida 25 bold",width=4,bg="grey",fg="white")
b.pack(side=LEFT)
b.bind("<Button-1>",click)

b=Button(f1, text=".", font="lucida 25 bold",width=4,bg="grey",fg="white")
b.pack(side=LEFT)
b.bind("<Button-1>",click)

f1.pack()

f1=Frame(window, bg="black")
b=Button(f1, text="+", font="lucida 25 bold",width=4,bg="grey",fg="white")
b.pack(side=LEFT)
b.bind("<Button-1>",click)

b=Button(f1, text="-", font="lucida 25 bold",width=4,bg="grey",fg="white")
b.pack(side=LEFT)
b.bind("<Button-1>",click)

b=Button(f1, text="/", font="lucida 25 bold",width=4,bg="grey",fg="white")
b.pack(side=LEFT)
b.bind("<Button-1>",click)

f1.pack()

f1=Frame(window, bg="black")
b=Button(f1, text="*", font="lucida 25 bold",width=4,bg="grey",fg="white")
b.pack(side=LEFT)
b.bind("<Button-1>",click)

b=Button(f1, text="c", font="lucida 25 bold",width=4,bg="grey",fg="white")
b.pack(side=LEFT)
b.bind("<Button-1>",click)

b=Button(f1, text="=", font="lucida 25 bold",width=4,bg="grey",fg="white")
b.pack(side=LEFT)
b.bind("<Button-1>",click)

f1.pack()
window.mainloop()