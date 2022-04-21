from cProfile import label
from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
import lib
import math
import matplotlib.pyplot as plt

#First View
czestotliwosc =1;
dmax = 1;
wsp_ochronny = 1;
h1 = 1;
sz_wiazki = 1;
cz_moc = 1; #Pomin
h2 =1;
srodowisko =1;
#Sec View
tl_fidera_Ant = 1; #Alfa
dl_fidera_Ant = 1; #F
Zysk_E_Ant_S_Bazowej = 1; #GB
Moc_Nadajnika = 1; #Pn
E_inf_min_db_uV_m = 1
E_inf_max_db_uV_m = 1
E_sup_min_db_uV_m = 1 
E_sup_max_db_uV_m = 1
h_nominalne_ponizej = 1
h_nominalne_powyzej = 1
f_min_Hz = 1
f_max_Hz = 1
#Graphs

#obliczenia
dl_skuteczna_anteny_polfalowej = 1.0;
Zwej = 50;
ch_war_nat_P = 1.0;
Zastepcza_moc_promieniowa = 1.0;
Poprawki_na_moc = Zastepcza_moc_promieniowa - 30;
Wartosc_nat_pola_elektrycznego_na_granicy_zasiegu = 1.0;
Epsilon_Nat_Pola_ele = 1.0;
Zasieg_zaklocajacy = 1.0;


class srodowisko:
    def __init__(self,master):
        global srodowisko
        srodowisko = tk.IntVar()
        sizes = (('Podmiejskie', 10),
                    ('Miejskie', 15),
                    ('Zabudowie Miejskie', 20))
            # radio buttons
        for size in sizes:
            r = ttk.Radiobutton(
            master,
            text=size[0],
            value=size[1],
            variable=srodowisko
                )
            r.pack(fill='x', padx=5, pady=5)


class First_view:

    def __init__(self, master):
       
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
        
        self.btn1 = Button(master, text="Zapisz", command=self.licz)

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
        
        self.btn1.grid(row=8,column=0,columnspan=2)\
        
        
    def licz(self):
        global czestotliwosc
        global dmax
        global wsp_ochronny
        global h1
        global sz_wiazki
        global cz_moc
        global h2
        czestotliwosc = float(self.czestotliwosc.get())
        dmax = float(self.dmax.get())
        wsp_ochronny = float(self.wspolczynnik_ochronny.get())
        h1 = float(self.h1.get())
        sz_wiazki = float(self.szerokosc_wiazki.get())
        cz_moc = float(self.czulosciowa_moc.get())
        h2 = float(self.h2.get())
        

class Sec_view:
    
    def __init__(self, master):
        
        self.label_info = Label(master,font=("Arial", 10), text="")
        
        self.label_tlumienie_fidera_Ant = Label(master, text="tłumienie jednostkowe fidera natenowego [dB/100m]: ")
        self.tlumienie_fidera_Ant = Entry(master)

        self.label_dlugosc_fidera_Ant = Label(master, text="długość fidera antenowego [m]: ")
        self.dlugosc_fidera_Ant = Entry(master)
        
        self.label_Zysk_E_Ant_S_Bazowej = Label(master, text="zysk energetyczny anteny stacji bazowej: ")
        self.Zysk_E_Ant_S_Bazowej = Entry(master)
      
        self.label_Moc_Nadajnika = Label(master, text="Moc nadajnika: ")
        self.Moc_Nadajnika = Entry(master)
        
        self.E_inf_min_db_uV_m_l = Label(master, text="E_inf_min_db_uV_m: ")
        self.E_inf_min_db_uV_m = Entry(master)
        
        self.E_inf_max_db_uV_m_l = Label(master, text="E_inf_max_db_uV_m: ")
        self.E_inf_max_db_uV_m = Entry(master)
        
        self.E_sup_min_db_uV_m_l = Label(master, text="E_sup_min_db_uV_m: ")
        self.E_sup_min_db_uV_m = Entry(master)
        
        self.E_sup_max_db_uV_m_l = Label(master, text="E_sup_max_db_uV_m: ")
        self.E_sup_max_db_uV_m = Entry(master)
        
        self.h_nominalne_ponizej_l = Label(master, text="h_nominalne_ponizej: ")
        self.h_nominalne_ponizej = Entry(master)
        
        self.h_nominalne_powyzej_l = Label(master, text="h_nominalne_powyzej: ")
        self.h_nominalne_powyzej = Entry(master)
        
        self.f_min_Hz_l = Label(master, text="f_min_Hz: ")
        self.f_min_Hz = Entry(master)
        
        self.f_max_Hz_l  = Label(master, text="f_max_Hz: ")
        self.f_max_Hz = Entry(master)
        
        self.greet_button = Button(master, text="Znajdz antenę", command=self.licz)
        self.greet_button2 = Button(master, text="Zapisz", command=self.zapisz)


        self.label_info.grid(row=1,rowspan=3, column=0, columnspan=3)
        self.label_tlumienie_fidera_Ant.grid(row=4,column=0)
        self.tlumienie_fidera_Ant.grid(row=4,column=1)
        
        self.label_dlugosc_fidera_Ant.grid(row=5,column=0)
        self.dlugosc_fidera_Ant.grid(row=5,column=1)
        
        self.label_Zysk_E_Ant_S_Bazowej.grid(row=6,column=0)
        self.Zysk_E_Ant_S_Bazowej.grid(row=6,column=1)
        
        self.label_Moc_Nadajnika.grid(row=7,column=0)
        self.Moc_Nadajnika.grid(row=7,column=1)
        
        self.E_inf_min_db_uV_m_l.grid(row=8,column=0)
        self.E_inf_min_db_uV_m.grid(row=8,column=1)
        
        self.E_inf_max_db_uV_m_l.grid(row=9,column=0)
        self.E_inf_max_db_uV_m.grid(row=9,column=1)
        
        self.E_sup_min_db_uV_m_l.grid(row=10,column=0)
        self.E_sup_min_db_uV_m.grid(row=10,column=1)
        
        self.E_sup_max_db_uV_m_l.grid(row=11,column=0)
        self.E_sup_max_db_uV_m.grid(row=11,column=1)
        
        self.h_nominalne_ponizej_l.grid(row=12,column=0)
        self.h_nominalne_ponizej.grid(row=12,column=1)
        
        self.h_nominalne_powyzej_l.grid(row=13,column=0)
        self.h_nominalne_powyzej.grid(row=13,column=1)
        
        self.f_min_Hz_l.grid(row=14,column=0)
        self.f_min_Hz.grid(row=14,column=1)
        
        self.f_max_Hz_l.grid(row=15,column=0)
        self.f_max_Hz.grid(row=15,column=1)
        
        self.greet_button.grid(row=16,column=0)
        self.greet_button2.grid(row=16,column=1)
        
    def licz(self):
        lib.Antena.Dobor_elementow
        txt = "czestotliwosc: [ "+str(czestotliwosc)+" ] dmax: [ "+str(dmax)+" ] wsp_ochronny: [ "+str(wsp_ochronny)+" ] h1: [ "+str(h1)+" ] Pomin: [ "+str(cz_moc)+" ] h2: [ "+str(h2)+" ]"
        self.label_info.config(text=txt)
    
    def zapisz(self):
        global tl_fidera_Ant #Alfa
        global dl_fidera_Ant #F
        global Zysk_E_Ant_S_Bazowej #GB
        global Moc_Nadajnika  #Pn
        global E_inf_min_db_uV_m
        global E_inf_max_db_uV_m
        global E_sup_min_db_uV_m
        global E_sup_max_db_uV_m
        global h_nominalne_ponizej
        global h_nominalne_powyzej
        global f_min_Hz
        global f_max_Hz
        tl_fidera_Ant = float(self.tlumienie_fidera_Ant.get())
        dl_fidera_Ant = float(self.dlugosc_fidera_Ant.get())
        Zysk_E_Ant_S_Bazowej = float(self.Zysk_E_Ant_S_Bazowej.get())
        Moc_Nadajnika = float(self.Moc_Nadajnika.get())
        E_inf_min_db_uV_m = float(self.E_inf_min_db_uV_m.get())
        E_inf_max_db_uV_m = float(self.E_inf_max_db_uV_m.get())
        E_sup_min_db_uV_m = float(self.E_sup_min_db_uV_m.get())
        E_sup_max_db_uV_m = float(self.E_sup_max_db_uV_m.get())
        h_nominalne_ponizej = float(self.h_nominalne_ponizej.get())
        h_nominalne_powyzej = float(self.h_nominalne_powyzej.get())
        f_min_Hz = float(self.f_min_Hz.get())
        f_max_Hz = float(self.f_max_Hz.get())
        
class obliczenia:
    def __init__(self, master):
        Pomin = math.pow(10,cz_moc/10);
        
        global dl_skuteczna_anteny_polfalowej
        global Zwej
        global ch_war_nat_P
        global Zastepcza_moc_promieniowa
        global Poprawki_na_moc 
        global Wartosc_nat_pola_elektrycznego_na_granicy_zasiegu 
        global Epsilon_Nat_Pola_ele 
        global Zasieg_zaklocajacy
        
        dl_skuteczna_anteny_polfalowej = lib.Antena.dlugosc_skuteczna_anteny_polfalowej(czestotliwosc)
        self.label_info = Label(master, text="Dlugosc skuteczna anteny polfalowej: "+str(dl_skuteczna_anteny_polfalowej))
        
        Zwej = 50
        self.label_info1 = Label(master, text="Rezystancja wejściowa: "+str(Zwej))
        
        E_min_czul = lib.Antena.E_min_czul(Zwej,dl_skuteczna_anteny_polfalowej,Pomin)
        self.label_info2 = Label(master, text="E min czułościowa: "+str(E_min_czul))
        
        ch_war_nat_P = lib.Antena.obl_chronionej_war_nat_P_Elektrycznego(E_min_czul,wsp_ochronny)
        self.label_info3 = Label(master, text="Dlugosc skuteczna anteny polfalowej: "+str(ch_war_nat_P))
        
        Zastepcza_moc_promieniowa = lib.Antena.Zastepcza_Moc_Promieniowa(Moc_Nadajnika,tl_fidera_Ant,dl_fidera_Ant,Zysk_E_Ant_S_Bazowej)
        self.label_info4 = Label(master, text="Dlugosc skuteczna anteny polfalowej: "+str(Zastepcza_moc_promieniowa))
        
        Wartosc_nat_pola_elektrycznego_na_granicy_zasiegu = lib.Antena.Wartosc_nat_pola_elektrycznego_na_granicy_zasiegu(czestotliwosc,E_inf_min_db_uV_m,E_sup_min_db_uV_m,h1,h2,h_nominalne_ponizej,h_nominalne_powyzej,Zastepcza_moc_promieniowa,int(srodowisko.get()),E_inf_max_db_uV_m,E_sup_max_db_uV_m,f_min_Hz,f_max_Hz)
        self.label_info5 = Label(master, text="Dlugosc skuteczna anteny polfalowej: "+str(Wartosc_nat_pola_elektrycznego_na_granicy_zasiegu))
        
        Epsilon_Nat_Pola_ele = lib.Antena.Epsilon_Nat_Pola_ele(Wartosc_nat_pola_elektrycznego_na_granicy_zasiegu,ch_war_nat_P)
        self.label_info6 = Label(master, text="Dlugosc skuteczna anteny polfalowej: "+str(Epsilon_Nat_Pola_ele))
        
        Zasieg_zaklocajacy = lib.Antena.Zasieg_zaklocajacy(E_min_czul,Wartosc_nat_pola_elektrycznego_na_granicy_zasiegu)
        self.label_info7 = Label(master, text="Dlugosc skuteczna anteny polfalowej: "+str(Zasieg_zaklocajacy))
        
        self.label_info.grid(row=1,column=0,columnspan=3)
        
        self.label_info1.grid(row=2,column=0,columnspan=3)
        
        self.label_info2.grid(row=3,column=0,columnspan=3)
        
        self.label_info3.grid(row=4,column=0,columnspan=3)
        
        self.label_info4.grid(row=5,column=0,columnspan=3)
        
        self.label_info5.grid(row=6,column=0,columnspan=3)
        
        self.label_info6.grid(row=7,column=0,columnspan=3)
        
        self.label_info7.grid(row=8,column=0,columnspan=3)
    
        




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






