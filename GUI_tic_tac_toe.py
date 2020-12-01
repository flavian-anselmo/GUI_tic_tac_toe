#MADE WITH LOVE BY ANSELMO FLAVIAN_@KIBABII_UNIVERSITY
from tkinter import*
from tkinter import messagebox
win = Tk()
win.resizable(False,False)
win.geometry("345x375")
win.title("Tic-Tac-Toe@ANSELMO")
v1=StringVar()
v2=StringVar()
v3=StringVar()
v4=StringVar()
v5=StringVar()
v6=StringVar()
v7=StringVar()
v8=StringVar()
v9=StringVar()
g1=v1.set("_")
g2=v2.set("_")
g3=v3.set("_")
g4=v4.set("_")
g5=v5.set("_")
g6=v6.set("_")
g7=v7.set("_")
g8=v8.set("_")
g9=v9.set("_")
player = True
p=1
tie = 0

def click1():
    global player,p,g1,b1,tie
    if player == True and p==1:
        v1.set("X")
        g1 ="X"
        player =False
        p=2
    elif player == False and p==2:
        v1.set("O")
        g1 = "O"
        player = True
        p=1
    b1 = Button(win, textvariable=v1, state=DISABLED,padx= 50,pady= 50,
                relief= RAISED,bg= "light green",fg="black").grid(row=0, column=0)
    tie += 1
    print(tie)
    check_row1()
    check_col()
    diagonal()

def click2():
    global player, p,g2,b2,tie
    if player == True and p==1:
        v2.set("X")
        g2 = "X"
        player = False
        p=2
    elif player == False and p==2:
        v2.set("O")
        g2 = "O"
        player = True
        p=1
    b2 = Button(win, textvariable=v2, state=DISABLED,padx= 50,pady= 50,
                relief= RAISED,bg= "light green",fg="black").grid(row=0, column=1)
    tie += 1
    print(tie)
    check_row1()
    check_col()

def click3():
    global player, p,g3,b3,tie
    if player == True and p==1:
        v3.set("X")
        g3 = "X"
        player = False
        p=2
    elif player == False and p==2:
        v3.set("O")
        g3 = "O"
        player = True
        p=1
    b3 = Button(win, textvariable=v3, state=DISABLED,padx= 50,pady= 50,
                relief= RAISED,bg= "light green",fg="black").grid(row=0, column=2)
    tie += 1
    print(tie)
    check_row1()
    check_col()
    diagonal()

def click4():
    global player, p,g4,b4,tie
    if player == True and p==1:
        v4.set("X")
        g4 ="X"
        player = False
        p=2
    elif player == False and p==2:
        v4.set("O")
        g4 = "O"
        player = True
        p=1
    b4 = Button(win, textvariable=v4, state=DISABLED,padx= 50,pady= 50,
                relief= RAISED,bg= "light green",fg="black").grid(row=1, column=0)
    tie += 1
    print(tie)
    check_row2()
    check_col()

def click5():
    global player, p,g5,b5,tie
    if player == True and p==1:
        v5.set("X")
        g5 = "X"
        player = False
        p=2
    elif player == False and p==2:
        v5.set("O")
        g5 = "O"
        player = True
        p=1
    b5 = Button(win, textvariable=v5, state=DISABLED,padx= 50,pady= 50,
                relief= RAISED,bg= "light green",fg="black").grid(row=1, column=1)
    tie += 1
    check_row2()
    check_col()
    diagonal()
#button_clicking
def click6():
    global player, p,g6,b6,tie
    if player == True and p==1:
        v6.set("X")
        g6 = "X"
        player = False
        p=2
    elif player == False and p==2:
        v6.set("O")
        g6 = "O"
        player = True
        p=1
    b6 = Button(win, textvariable=v6, state=DISABLED,padx= 50,pady= 50,
                relief= RAISED,bg= "light green",fg="black").grid(row=1, column=2)
    tie += 1
    print(tie)
    check_row2()
    check_col()

def click7():
    global player, p,g7,b7,tie
    if player == True and p==1:
        v7.set("X")
        g7 = "X"
        player = False
        p=2
    elif player == False and p==2:
        v7.set("O")
        g7 = "O"
        player = True
        p=1
    b7 = Button(win, textvariable=v7, state=DISABLED,padx= 50,pady= 50,
                relief= RAISED,bg= "light green",fg="black").grid(row=2, column=0)
    tie += 1
    print(tie)
    check_row3()
    check_col()
    diagonal()

def click8():
    global player, p,g8,b8,tie
    if player == True and p==1:
        v8.set("X")
        g8 = "X"
        player = False
        p=2
    elif player == False and p==2:
        v8.set("O")
        g8 = "O"
        player = True
        p=1
    b8 = Button(win, textvariable=v8, state=DISABLED,padx= 50,pady= 50,
                relief= RAISED,bg= "light green",fg="black").grid(row=2, column=1)
    tie += 1
    print(tie)
    check_row3()
    check_col()

def click9():
    global player, p,g9,b9,tie
    if player == True and p==1:
        v9.set("X")
        g9= "X"
        player = False
        p=2
    elif player == False and p==2:
        v9.set("O")
        g9 = "O"
        player = True
        p=1
    b9 = Button(win, textvariable=v9, state=DISABLED,padx= 50,pady= 50,
                relief= RAISED,bg= "light green",fg="black").grid(row=2, column=2)
    tie += 1
    print(tie)
    check_row3()
    check_col()
    diagonal()
#CHECK FOR WINNER
def check_row1():#row1
    if g1 == "X" and g2 == "X"and g3 == "X":
         messagebox.showinfo("msg_box", 'player x won!')
    elif g1 == "O" and g2 == "O" and g3 == "O":
        messagebox.showinfo("msg_box", 'player o won!')
    draw()
def check_row2():#row2
    if g4 == "X" and g5 == "X" and g6 == "X":
        messagebox.showinfo("msg_box", 'player x won!')
    elif g4 == "O" and g5 == "O" and g6 == "O":
        messagebox.showinfo("msg_box", 'player o won!')
    draw()
def check_row3():#row3
    if g7== "X" and g8 == "X" and g9 =="X":
        messagebox.showinfo("msg_box", 'player x won!')
    elif g7 == "O" and g8 == "O" and g9 == "O":
        messagebox.showinfo("msg_box", 'player o  won!')
    draw()
def check_col():#column_chek
    if g1== "X" and g4 == "X" and g7 =="X":
        messagebox.showinfo("msg_box", 'player x won!')
    elif g1 == "O" and g4 == "O" and g7 == "O":
        messagebox.showinfo("msg_box", 'player o  won!')
    elif g2== "X" and g5 == "X" and g8 =="X":
        messagebox.showinfo("msg_box", 'player x won!')
    elif g2== "O" and g5 == "O" and g8== "O":
        messagebox.showinfo("msg_box", 'player o  won!')
    elif g3== "X" and g6 == "X" and g9 =="X":
        messagebox.showinfo("msg_box", 'player x won!')
    elif g3 == "O" and g6 == "O" and g9 == "O":
        messagebox.showinfo("msg_box", 'player o  won!')
    draw()
def diagonal():#diagonal_check
    if g1 == "X" and g5 == "X" and g9 == "X":
        messagebox.showinfo("msg_box", 'player x  won!')
    elif g1 == "O" and g5 == "O" and g9 == "O":
        messagebox.showinfo("msg_box", 'player o won!')
    if g7 == "X" and g5 == "X" and g3 == "X":
        messagebox.showinfo("msg_box", 'player x  won!')
    elif g7 == "O" and g5 == "O" and g3 == "O":
        messagebox.showinfo("msg_box", 'player o  won!')
    draw()

def draw():#checks for a tie
    if tie == 9:
        messagebox.showinfo("msg_box", "it was a tie!")

b1 = Button(win,textvariable = v1,command = click1,padx= 50,pady= 50,relief= RAISED,bg= "green",fg="black")\
    .grid(row = 0 , column = 0)
b2 = Button(win,textvariable = v2,command = click2,padx= 50,pady= 50,relief= RAISED,bg= "green",fg="black")\
    .grid(row = 0 , column = 1)
b3 = Button(win,textvariable = v3,command = click3,padx= 50,pady= 50,relief= RAISED,bg= "green",fg="black")\
    .grid(row = 0 , column = 2)
b4 = Button(win,textvariable = v4,command = click4,padx= 50,pady= 50,relief= RAISED,bg= "green",fg="black")\
    .grid(row = 1 , column = 0)
b5 = Button(win,textvariable = v5,command = click5,padx= 50,pady= 50,relief= RAISED,bg= "green",fg="black")\
    .grid(row = 1 , column = 1)
b6 = Button(win,textvariable = v6,command = click6,padx= 50,pady= 50,relief= RAISED,bg= "green",fg="black")\
    .grid(row = 1 , column = 2)
b7 = Button(win,textvariable = v7,command = click7,padx= 50,pady= 50,relief= RAISED,bg= "green",fg="black")\
    .grid(row = 2 , column = 0)
b8 = Button(win,textvariable = v8,command = click8,padx= 50,pady= 50,relief= RAISED,bg= "green",fg="black")\
    .grid(row = 2 , column = 1)
b9 = Button(win,textvariable = v9,command = click9,padx= 50,pady= 50,relief= RAISED,bg= "green",fg="black")\
    .grid(row = 2 , column = 2)
win.mainloop()