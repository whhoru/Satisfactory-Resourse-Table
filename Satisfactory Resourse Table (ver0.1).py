import tkinter as tk
from tkinter import *

root = tk.Tk()
root.geometry('400x270')
root.resizable(False, False)

root.title('Satisfactory Resourse Table (ver0.1)')

canvas = Canvas(root, width=320, height=320)
canvas.pack()

ur_image=PhotoImage(file='Cable.jpg')
ur_label=Label(root)
ur_label.image = ur_image
ur_label['image'] = ur_label.image
ur_label.place(x = 5, y = 10)
ent = Entry()
ent.place(x = 55, y = 25)

ur_image=PhotoImage(file='Concrete.jpg')
ur_label=Label(root)
ur_label.image = ur_image
ur_label['image'] = ur_label.image
ur_label.place(x = 5, y = 60)
ent = Entry()
ent.place(x = 55, y = 75)

ur_image=PhotoImage(file='Encased_Industrial_Beam.jpg')
ur_label=Label(root)
ur_label.image = ur_image
ur_label['image'] = ur_label.image
ur_label.place(x = 5, y = 110)
ent = Entry()
ent.place(x = 55, y = 125)

ur_image=PhotoImage(file='Iron_Plate.jpg')
ur_label=Label(root)
ur_label.image = ur_image
ur_label['image'] = ur_label.image
ur_label.place(x = 5, y = 160)
ent = Entry()
ent.place(x = 55, y = 175)

ur_image=PhotoImage(file='Iron_Rod.jpg')
ur_label=Label(root)
ur_label.image = ur_image
ur_label['image'] = ur_label.image
ur_label.place(x = 5, y = 210)
ent = Entry()
ent.place(x = 55, y = 225)

#--------------------

ur_image=PhotoImage(file='Modular_Frame.jpg')
ur_label=Label(root)
ur_label.image = ur_image
ur_label['image'] = ur_label.image
ur_label.place(x = 205, y = 10)
ent = Entry()
ent.place(x = 255, y = 25)

ur_image=PhotoImage(file='Reinforced_Iron_Plate.jpg')
ur_label=Label(root)
ur_label.image = ur_image
ur_label['image'] = ur_label.image
ur_label.place(x = 205, y = 60)
ent = Entry()
ent.place(x = 255, y = 75)

ur_image=PhotoImage(file='Rotor.jpg')
ur_label=Label(root)
ur_label.image = ur_image
ur_label['image'] = ur_label.image
ur_label.place(x = 205, y = 110)
ent = Entry()
ent.place(x = 255, y = 125)

ur_image=PhotoImage(file='Steel_Beam.jpg')
ur_label=Label(root)
ur_label.image = ur_image
ur_label['image'] = ur_label.image
ur_label.place(x = 205, y = 160)
ent = Entry()
ent.place(x = 255, y = 175)

ur_image=PhotoImage(file='Steel_Pipe.jpg')
ur_label=Label(root)
ur_label.image = ur_image
ur_label['image'] = ur_label.image
ur_label.place(x = 205, y = 210)
ent = Entry()
ent.place(x = 255, y = 225)

root.mainloop()