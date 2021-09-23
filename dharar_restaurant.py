from tkinter import *

root = Tk()

#-----Making the window----

root.geometry('700x500')
root.minsize(700,500)
root.maxsize(710,510)

#------Title of the window----
root.title('Anas Dharar Restaurant')

#-----function to calculate the total bill-------
def calculate():
    vp= e1.get()
    samosa = e2.get()
    idli = e3.get()
    paratha = e4.get()

    if vp=='':
        vp=0
    if samosa=='':
        samosa=0
    if idli=='':
        idli=0
    if paratha=='':
        paratha=0
    
    price1 = int(vp)*12
    price2 = int(samosa)*15
    price3 = int(idli)*10
    price4 = int(paratha)*20
    amount = price1+price2+price3+price4
    text_amount= 'Your total bill is',amount
    total = Label(root, text=text_amount, font='cambria 20 bold')
    total.place(x=20, y=350)
    



#---Heading Label------
header = Label(root, text='Dharar Restaurant', font='Cambria 30 italic')
header.place(x=350, y=20, anchor='center')
#-------------menu section---------
menu_heading = Label(root, text="MENU", font="algerian 28 underline")
menu_heading.place(x=550, y=70)

menu_item1 = Label(root, text="Vada Pav          Rs. 12", font="times 15 italic")
menu_item1.place(x=450, y=120)

menu_item2 = Label(root, text="Samosa            Rs. 15", font="times 15 italic")
menu_item2.place(x=450, y=140)

menu_item3 = Label(root, text="Idli              Rs. 10", font="times 15 italic")
menu_item3.place(x=450, y=160)

menu_item4 = Label(root, text="Aloo Paratha      Rs. 20", font="times 15 italic")
menu_item4.place(x=450, y=180)


#--------------- Billing Section ----------------------------

#Heading..........
header2 = Label(root, text="Select The Items", font="algerian 20 italic")
header2.place(x=70, y=70)

#Items............
item1 = Label(root, text="Vada Pav", font="times 18")
item1.place(x=20, y=120)

e1 = Entry(root)
e1.place(x=20,y=150)
#---------------------
item2 = Label(root, text="Samosa", font="times 18")
item2.place(x=250, y=120)

e2 = Entry(root)
e2.place(x=250,y=150)
#--------------------
item3 = Label(root, text="Idli", font="times 18")
item3.place(x=20, y=200)

e3 = Entry(root)
e3.place(x=20,y=230)
#-------------------
item4 = Label(root, text="Aloo Paratha", font="times 18")
item4.place(x=250, y=200)

e4 = Entry(root)
e4.place(x=250,y=230)
#------------------

#-----Calculating button------------
b = Button(root, text='Bill',width=20, command=calculate)
b.place(x=100,y=300)

root.mainloop()