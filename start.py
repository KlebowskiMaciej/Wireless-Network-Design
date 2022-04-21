from tkinter import *
from tkinter import ttk

from tkinter.messagebox import showinfo
import math
import view

#Window set
window = Tk()
window.title("Projekt PSB")
icon = PhotoImage(file='icon.png')
window.iconphoto(True,icon)
notebook = ttk.Notebook(window)

#Tab Set
srodowisko = Frame(notebook)
parametry = Frame(notebook)
parametry2 = Frame(notebook)
Wyniki = Frame(notebook)

notebook.add(srodowisko,text="Srodowisko")
notebook.add(parametry,text="Parametry")
notebook.add(parametry2,text="Parametry2")
notebook.add(Wyniki,text="Wyniki")
notebook.pack(expand=True,fill="both")

view.srodowisko(srodowisko)
view.First_view(parametry)
view.Sec_view(parametry2)
view.obliczenia(Wyniki)






#Wykresiki końcowe
#view.wykres_trzy_dwa(wykresy)


window.mainloop()

