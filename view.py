from cProfile import label
from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
import lib
import matplotlib.pyplot as plt

class srodowisko():
    def __init__(self,master):
        self.master = master
        selected_size = tk.IntVar()
        sizes = (('Podmiejskie', 10),
                    ('Miejskie', 15),
                    ('Zabudowie Miejskie', 20))
            # radio buttons
        for size in sizes:
            r = ttk.Radiobutton(
            master,
            text=size[0],
            value=size[1],
            variable=selected_size
                )
            r.pack(fill='x', padx=5, pady=5)


class First_view:
    def __init__(self, master):
        self.master = master
       
        
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
        
        self.btn1 = Button(master, text="Znajdz antenę", command=self.licz)

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
        
        self.btn1.grid(row=8,column=0,columnspan=2)
        
    def licz(self):
        print("essa")

class Sec_view:
    def __init__(self, master):
        self.master = master
        
        self.label_info = Label(master, text="sssssssssssss")
        
        self.label_tlumienie_fidera_Ant = Label(master, text="tłumienie jednostkowe fidera natenowego [dB/100m]: ")
        self.tlumienie_fidera_Ant = Entry(master)

        self.label_dlugosc_fidera_Ant = Label(master, text="długość fidera antenowego [m]: ")
        self.dlugosc_fidera_Ant = Entry(master)
        
        self.label_Zysk_E_Ant_S_Bazowej = Label(master, text="zysk energetyczny anteny stacji bazowej: ")
        self.Zysk_E_Ant_S_Bazowej = Entry(master)
      
        self.label_Moc_Nadajnika = Label(master, text="Moc nadajnika: ")
        self.Moc_Nadajnika = Entry(master)
        
        self.greet_button = Button(master, text="Znajdz antenę", command=lib.Antena.Dobor_elementow)


        self.label_info.grid(row=1,rowspan=3, column=0, columnspan=3)
        self.label_tlumienie_fidera_Ant.grid(row=4,column=0)
        self.tlumienie_fidera_Ant.grid(row=4,column=1)
        
        self.label_dlugosc_fidera_Ant.grid(row=5,column=0)
        self.dlugosc_fidera_Ant.grid(row=5,column=1)
        
        self.label_Zysk_E_Ant_S_Bazowej.grid(row=6,column=0)
        self.Zysk_E_Ant_S_Bazowej.grid(row=6,column=1)
        
        self.label_Moc_Nadajnika.grid(row=7,column=0)
        self.Moc_Nadajnika.grid(row=7,column=1)
        
        self.greet_button.grid(row=8,column=0,columnspan=2)


class wykres_trzy_dwa():
    def __init__(self, master):
        self.master = master
        
        E_min_chron = [23.074,23.074,23.074,23.074,23.074,23.074,23.074,23.074,23.074,23.074,23.074,23.074,23.074,23.074,23.074,23.074,23.074,23.074,23.074,23.074]
        E_min_chron_alfa1 = [15.305728261938,18.3160282185778,20.0769408091346,21.3263281752176,22.2954283052982,23.0872407657744,23.7567086620805,24.3366281318574,24.8481533563312,25.305728261938,25.7196551135202,26.0975407224142,26.4451617850063,26.7670086187203,27.0666408524948,27.3469280884972,27.6102174757207,27.858453312971,28.0932642714663,28.3160282185778]
        E_min_chron_alfa2 = [15.305728261938,18.3160282185778,20.0769408091346,21.3263281752176,22.2954283052982,23.0872407657744,23.7567086620805,24.3366281318574,24.8481533563312,25.305728261938,25.7196551135202,26.0975407224142,26.4451617850063,26.7670086187203,27.0666408524948,27.3469280884972,27.6102174757207,27.858453312971,28.0932642714663,28.3160282185778]
        E_min_chron_alfa3 = [15.305728261938,18.3160282185778,20.0769408091346,21.3263281752176,22.2954283052982,23.0872407657744,23.7567086620805,24.3366281318574,24.8481533563312,25.305728261938,25.7196551135202,26.0975407224142,26.4451617850063,26.7670086187203,27.0666408524948,27.3469280884972,27.6102174757207,27.858453312971,28.0932642714663,28.3160282185778]
        E_min_chron_alfa4 = [15.305728261938,18.3160282185778,20.0769408091346,21.3263281752176,22.2954283052982,23.0872407657744,23.7567086620805,24.3366281318574,24.8481533563312,25.305728261938,25.7196551135202,26.0975407224142,26.4451617850063,26.7670086187203,27.0666408524948,27.3469280884972,27.6102174757207,27.858453312971,28.0932642714663,28.3160282185778]
        PN = [0.5,1,1.5,2,2.5,3,3.5,4,4.5,5,5.5,6,6.5,7,7.5,8,8.5,9,9.5,10]
        plt.plot(PN, E_min_chron, label = "E min chron")
        plt.plot(PN, E_min_chron_alfa1, label = "α=2,492")
        plt.plot(PN, E_min_chron_alfa2, label = "α=2,583")
        plt.plot(PN, E_min_chron_alfa3, label = "α=2,977")
        plt.plot(PN, E_min_chron_alfa4, label = "α=3,235")
        plt.xlabel('PN')
        plt.ylabel('y - axis')
        plt.title('3.2.1')
        plt.legend()
        plt.show()





