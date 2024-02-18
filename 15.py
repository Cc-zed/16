from tkinter import *


def Banana_Mania():
    label.config(text="Banana Mania", bg="#fae7b5", fg="Black")
    entry.delete(0,END)
    entry.insert(0,"#fae7b5")
    root['background']='#fae7b5'

def Pale_Spring_Bud():
    label.config(text="Pale Spring Bud", bg="#ecebbd", fg="Black")
    entry.delete(0,END)
    entry.insert(0,"#ecebbd")
    root['background']='#ecebbd'

def Oxblood():
    label.config(text="Oxblood", bg="#4a0000", fg="White")
    entry.delete(0,END)
    entry.insert(0,"#4a0000")
    root['background']='#4a0000'

def Pansy_Purple():
    label.config(text="Pansy Purple", bg="#78184a", fg="White")
    entry.delete(0,END)
    entry.insert(0,"#78184a")
    root['background']='#78184a'

def VioletRed3():
    label.config(text="VioletRed3", bg="#cd3278", fg="Black")
    entry.delete(0,END)
    entry.insert(0,"#cd3278")
    root['background']='#cd3278'

def Yellow_Pantone():
    label.config(text="Yellow Pantone", bg="#fedf00", fg="Black")
    entry.delete(0,END)
    entry.insert(0,"#fedf00")
    root['background']='#fedf00'

def Tea_Green():
    label.config(text="Tea Green", bg="#d0f0c0", fg="Black")
    entry.delete(0,END)
    entry.insert(0,"#d0f0c0")
    root['background']='#d0f0c0'

def Teal_Blue():
    label.config(text="Teal Blue", bg="#367588", fg="White")
    entry.delete(0,END)
    entry.insert(0,"#367588")
    root['background']='#367588'

def Warm_Black():
    label.config(text="Warm Black", bg="#004242", fg="White")
    entry.delete(0,END)
    entry.insert(0,"#004242")
    root['background']='#004242'

def Prussian_Blue():
    label.config(text="Prussian Blue", bg="#003153", fg="White")
    entry.delete(0,END)
    entry.insert(0,"#003153")
    root['background']='#003153'


root = Tk()
root.title("Color Picker")
root.geometry("650x900")

label = Label(root, anchor='c')
label.pack()


entry = Entry(root, justify='center', bd=5, width= 40)
entry.pack(pady= 5)

l = Label(root, text = "Banana Mania", bg="#fae7b5", padx=12, pady=5)
l.place(relx = 0.01, rely = 0.075)

button1 = Button(root, width=50, bg='#fae7b5', fg='white', command=Banana_Mania)
button1.pack()

l2 = Label(root, text = "Pale Spring Bud", bg="#ecebbd", padx=12, pady=5)
l2.place(relx = 0.01, rely = 0.112)

button2 = Button(root, width=50, bg='#ecebbd', fg='white', command=Pale_Spring_Bud)
button2.pack()

l3 = Label(root, text = "Oxblood", bg="#4a0000", padx=29, pady=5, fg="White")
l3.place(relx = 0.01, rely = 0.147)

button3 = Button(root, width=50, bg='#4a0000', fg='white', command=Oxblood)
button3.pack()

l4 = Label(root, text = "VioletRed3", bg="#78184a", padx=22, pady=5, fg="White")
l4.place(relx = 0.01, rely = 0.183)

button4 = Button(root, width=50, bg='#78184a', fg='white', command=Pansy_Purple)
button4.pack()

l5 = Label(root, text = "VioletRed3", bg="#cd3278", padx=22, pady=5)
l5.place(relx = 0.01, rely = 0.219)

button5 = Button(root, width=50, bg='#cd3278', fg='white', command=VioletRed3)
button5.pack()

l6 = Label(root, text = "Yellow Pantone", bg="#fedf00", padx=12, pady=5)
l6.place(relx = 0.01, rely = 0.255)

button6 = Button(root, width=50, bg='#fedf00', fg='white', command=Yellow_Pantone)
button6.pack()

l7 = Label(root, text = "Tea Green", bg="#d0f0c0", padx=25, pady=5.5)
l7.place(relx = 0.01, rely = 0.292)

button7 = Button(root, width=50, bg='#d0f0c0', fg='white', command=Tea_Green)
button7.pack()

l8 = Label(root, text = "Teal Blue", bg="#367588", padx=28, pady=5, fg="White")
l8.place(relx = 0.01, rely = 0.330)

button8 = Button(root, width=50, bg='#367588', fg='white', command=Teal_Blue)
button8.pack()

l9 = Label(root, text = "Warm Black", bg="#004242", padx=19, pady=5, fg="White")
l9.place(relx = 0.01, rely = 0.365)

button9 = Button(root, width=50, bg='#004242', fg='white', command=Warm_Black)
button9.pack()

l10 = Label(root, text = "Prussian Blue", bg="#003153", padx=15, pady=5, fg="White")
l10.place(relx = 0.01, rely = 0.402)

button10 = Button(root, width=50, bg='#003153', fg='white', command=Prussian_Blue)
button10.pack()


root.mainloop()
