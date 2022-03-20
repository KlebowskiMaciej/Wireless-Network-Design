from tkinter import *


class First_view:
    def __init__(self, master):
        self.master = master
        master.title("Projekt PSB")
        icon = PhotoImage(file='icon.png')
        master.iconphoto(True,icon)
        
        self.label_f = Label(master, text="Częstotliwość [Hz]: ")
        self.czestotliwosc = Entry(master)

        self.label_dmax = Label(master, text="Zasięg uzyteczny [km]: ")
        self.dmax = Entry(master)
        
        self.label_A = Label(master, text="Współczynnik ochronny [dB]: ")
        self.wspolczynnik_ochronny = Entry(master)
      
        self.label_h1 = Label(master, text="Wysokość zawieszenia antenty stacji bazowej [m n.p.t]: ")
        self.h1 = Entry(master)
        
        self.label_szerokosc_wiazki = Label(master, text="Szerokość wiązki głównej anteny nadawczej [°]: ")
        self.szerokosc_wiazki = Entry(master)
        
        self.label_czulosciowa_moc = Label(master, text="Czułościowa moc odbiornika [dBm]: ")
        self.czulosciowa_moc = Entry(master)
        
        self.label_h2 = Label(master, text="Wysokość zawieszenia terminala uzytkownika [m n.p.t]: ")
        self.h2 = Entry(master)
        
        self.greet_button = Button(master, text="Dalej!", command=self.Licz)
        self.close_button = Button(master, text="Zamknij", command=master.quit)

        self.label_f.grid(row=1,column=0)
        self.czestotliwosc.grid(row=1,column=1)
        
        self.label_dmax.grid(row=2,column=0)
        self.dmax.grid(row=2,column=1)
        
        self.label_A.grid(row=3,column=0)
        self.wspolczynnik_ochronny.grid(row=3,column=1)
        
        self.label_h1.grid(row=4,column=0)
        self.h1.grid(row=4,column=1)
        
        self.label_szerokosc_wiazki.grid(row=5,column=0)
        self.szerokosc_wiazki.grid(row=5,column=1)
        
        self.label_czulosciowa_moc.grid(row=6,column=0)
        self.czulosciowa_moc.grid(row=6,column=1)
        
        self.label_h2.grid(row=7,column=0)
        self.h2.grid(row=7,column=1)
        
        self.greet_button.grid(row=8,column=0)
        self.close_button.grid(row=8,column=1)

    def Licz(self):
        print("Greetings!")


class Sec_view:
    def __init__(self, master):
        self.master = master
        master.title("Projekt PSB")
        icon = PhotoImage(file='icon.png')
        master.iconphoto(True,icon)
        
        self.label_tlumienie_fidera_Ant = Label(master, text="tłumienie jednostkowe fidera natenowego [dB/100m]: ")
        self.tlumienie_fidera_Ant = Entry(master)

        self.label_dlugosc_fidera_Ant = Label(master, text="długość fidera antenowego [m]: ")
        self.dlugosc_fidera_Ant = Entry(master)
        
        self.label_Zysk_E_Ant_S_Bazowej = Label(master, text="zysk energetyczny anteny stacji bazowej: ")
        self.Zysk_E_Ant_S_Bazowej = Entry(master)
      
        self.label_Moc_Nadajnika = Label(master, text="Moc nadajnika: ")
        self.Moc_Nadajnika = Entry(master)
        
        self.greet_button = Button(master, text="Dalej!", command=self.Licz)
        self.close_button = Button(master, text="Zamknij", command=master.quit)

        self.label_tlumienie_fidera_Ant.grid(row=1,column=0)
        self.tlumienie_fidera_Ant.grid(row=1,column=1)
        
        self.label_dlugosc_fidera_Ant.grid(row=2,column=0)
        self.dlugosc_fidera_Ant.grid(row=2,column=1)
        
        self.label_Zysk_E_Ant_S_Bazowej.grid(row=3,column=0)
        self.Zysk_E_Ant_S_Bazowej.grid(row=3,column=1)
        
        self.label_Moc_Nadajnika.grid(row=4,column=0)
        self.Moc_Nadajnika.grid(row=4,column=1)
        
        self.greet_button.grid(row=5,column=0)
        self.close_button.grid(row=5,column=1)

    def Licz(self):
        print("Greetings!")


root = Tk()
my_gui = First_view(root)
root.mainloop()