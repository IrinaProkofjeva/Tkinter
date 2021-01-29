from tkinter import ttk
from tkinter import scrolledtext
from tkinter.filedialog import *
import fileinput 
from tkinter.messagebox import *


root=Tk()
root.geometry("400x300")
root.title("Elemendid Tkienteris")

tabs=ttk.Notebook(root)
texts=["Esimene", "Teine", "Kolmas", "Neljas", "Viies", "Kuues", "Seitsmes", "Kaheksas"]

#for i in range(8): #len(texts)
#    tab=Frame(tabs)
#    tabs.add(tab,text=texts[i])
tab1=Frame(tabs)
tab2=Frame(tabs)
tab3=Frame(tabs)
tab4=Frame(tabs)
tabs.add(tab1,text="Esimene")
tabs.add(tab2,text="Teine")
tabs.add(tab3,text="Kolmas")
tabs.add(tab4,text="Neljas")

M=Menu(root)
root.config(menu=M)
m1=Menu(M,tearoff=1)
M.add_cascade(label="Tabs",menu=m1)
m1.add_command(label="Tab1",accelerator="Command+V",command=lambda:funktion(0))
m1.add_separator() #Делитель
m1.add_command(label="Tab2",command=lambda:funktion(1))
m1.add_separator() #Делитель
m1.add_command(label="Tab3",command=lambda:funktion(2))
m1.add_separator() #Делитель
m1.add_command(label="Tab4",command=lambda:funktion(3))

m2=Menu(M,tearoff=2)
M.add_cascade(label="Colors",menu=m2)
m2.add_command(label="Green",command=lambda:root.config(bg="green"))
m2.add_separator() #Делитель
m2.add_command(label="Yellow",command=lambda:root.config(bg="yellow"))
m2.add_separator() #Делитель
m2.add_command(label="Blue",command=lambda:root.config(bg="blue"))
m2.add_separator() #Делитель
m2.add_command(label="Red",command=lambda:root.config(bg="red"))
m2.add_separator() #Делитель
m2.add_command(label="Lightblue",command=lambda:root.config(bg="lightblue"))
m2.add_separator() #Делитель
m2.add_command(label="Purple",command=lambda:root.config(bg="purple"))
m2.add_separator() #Делитель
m2.add_command(label="Pink",command=lambda:root.config(bg="pink"))
m2.add_separator() #Делитель
m2.add_command(label="Lightgreen",command=lambda:root.config(bg="lightgreen"))
m2.add_separator() #Делитель
m2.add_command(label="Lightblue",command=lambda:root.config(bg="lightblue"))
m2.add_separator() #Делитель
m2.add_command(label="Lightyellow",command=lambda:root.config(bg="lightyellow"))


m3=Menu(M,tearoff=3)
M.add_cascade(label="Image",menu=m3)
m3.add_command(label="Cat",command=lambda:image_cat("angrycat.png"))
m3.add_separator() #Делитель
m3.add_command(label="Dog",command=lambda:image_dog("dog.png"))
m3.add_separator() #Делитель
m3.add_command(label="Rabbit",command=lambda:image_rabbit("Mead-Peter-Rabbit(1).png"))
m3.add_separator() #Делитель
m3.add_command(label="Raccoon",command=lambda:image_raccoon("raccoon.png"))



btn_open=Button(tab1,text="Open")
btn_save=Button(tab1,text="Save")
btn_exit=Button(tab1,text="Exit")
txt_box=scrolledtext.ScrolledText(tab1,width=40,height=5)
txt_box.grid(row=0,column=0,columnspan=3)
btn_open.grid(row=1,column=0)
btn_save.grid(row=1,column=1)
btn_exit.grid(row=1,column=2)

def funktion(a):
    tabs.select(a)

def open_():
    file=askopenfilename() #Название файла
    for text in fileinput.input(file):
        txt_box.insert(0.0,text)

def save_():
    file=askopenfile(mode="w",defaultextension=((".txt"),(".docx")),filetypes=(("Notepad",".txt"),("Word",".docx")))
    t=txt_box.get(0.0,END)
    file.write(t)
    file.close()

def exit_():
    if askyesno("Exit","Yes/No"):
        showinfo("Exit","Message: Yes")
        root.destroy()
    else:
        showninfo("No")

can=Canvas(tab2,width=300,height=200)
can.pack()

def image_cat(name):
    global img
    tabs.select(1)
    img=PhotoImage(file=name).subsample(4)
    can-create_image(10.10,image=img,anchor=NW)



tabs.pack(fill="both")

root.mainloop()
