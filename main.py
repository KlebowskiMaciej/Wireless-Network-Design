from tkinter import *
import tkinter as tk

window = tk.Tk()
import fun


#Window settings
window.title("Parametry projekt PSB")
window.geometry("600x400")
window.config(bg="black")
icon = PhotoImage(file='icon.png')
window.iconphoto(True,icon)

label_f = tk.Label(window, text = 'f [Hz]: ', font=('Arial',10),fg='#ffffff',bg='#000000')
f_var = Spinbox(window, from_=440000000, to=8888888888888888888,font=('Arial',10),fg='#ffffff', bg='#000000', highlightbackground = '#000000',highlightcolor= '#000000',highlightthickness=2,bd =1)

label_dmax = tk.Label(window, text = 'dmax [m]: ', font=('Arial',10),fg='#ffffff',bg='#000000')
dmax_var = Spinbox(window, from_=7000, to=8888888888888888888,font=('Arial',10),fg='#ffffff', bg='#000000', highlightbackground = '#000000',highlightcolor= '#000000',highlightthickness=2,bd =1)

label_A = tk.Label(window, text = 'A [dB]: ', font=('Arial',10),fg='#ffffff',bg='#000000')
A_var = Spinbox(window, from_=14, to=8888888888888888888,font=('Arial',10),fg='#ffffff', bg='#000000', highlightbackground = '#000000',highlightcolor= '#000000',highlightthickness=2,bd =1)

label_h1 = tk.Label(window, text = 'h1 [m n.p.t]: ', font=('Arial',10),fg='#ffffff',bg='#000000')
h1_var = Spinbox(window, from_=30, to=8888888888888888888,font=('Arial',10),fg='#ffffff', bg='#000000', highlightbackground = '#000000',highlightcolor= '#000000',highlightthickness=2,bd =1)

label_s_w = tk.Label(window, text = 'Sz. wiazki glownej[°]: ', font=('Arial',10),fg='#ffffff',bg='#000000')
s_w_var = Spinbox(window, from_=60, to=8888888888888888888,font=('Arial',10),fg='#ffffff', bg='#000000', highlightbackground = '#000000',highlightcolor= '#000000',highlightthickness=2,bd =1)

label_c_m = tk.Label(window, text = 'cz. mocowa odb. [dBm]: ', font=('Arial',10),fg='#ffffff',bg='#000000')
c_m_var = Spinbox(window, from_=-110, to=8888888888888888888,font=('Arial',10),fg='#ffffff', bg='#000000', highlightbackground = '#000000',highlightcolor= '#000000',highlightthickness=2,bd =1)

label_h2 = tk.Label(window, text = 'h2 [m n.p.t]: ', font=('Arial',10),fg='#ffffff',bg='#000000')
h2_var  = Spinbox(window, from_=1.5, to=8888888888888888888,font=('Arial',10),fg='#ffffff', bg='#000000', highlightbackground = '#000000',highlightcolor= '#000000',highlightthickness=2,bd =1)
##############

label_elementy = tk.Label(window, text = 'Wybrane elementy: ', font=('Arial',20),fg='#ffffff',bg='#000000')

label_Pn = tk.Label(window, text = 'moc nadajnika [dBW]: ', font=('Arial',10),fg='#ffffff',bg='#000000')
Pn_var = Spinbox(window, from_=1, to=8888888888888888888,font=('Arial',10),fg='#ffffff', bg='#000000', highlightbackground = '#000000',highlightcolor= '#000000',highlightthickness=2,bd =1)

label_alfa = tk.Label(window, text = 'tlumienie jednostkowe fidera natenowego [dB/100m]: ', font=('Arial',10),fg='#ffffff',bg='#000000')
alfa_fidera_antenowego_var = Spinbox(window, from_=1, to=8888888888888888888,font=('Arial',10),fg='#ffffff', bg='#000000', highlightbackground = '#000000',highlightcolor= '#000000',highlightthickness=2,bd =1)

label_F_elementu = tk.Label(window, text = 'dlugosc fidera antenowego [m]: ', font=('Arial',10),fg='#ffffff',bg='#000000')
F_dlugosc_fidera_antenowego_var = Spinbox(window, from_=1, to=8888888888888888888,font=('Arial',10),fg='#ffffff', bg='#000000', highlightbackground = '#000000',highlightcolor= '#000000',highlightthickness=2,bd =1)

label_alfa_jumpera= tk.Label(window, text = 'tlumienie jednostkowe jumpera antenowego [dB/100m]: ', font=('Arial',10),fg='#ffffff',bg='#000000')
alfa_jumpera_antenowego_var  = Spinbox(window, from_=1, to=8888888888888888888,font=('Arial',10),fg='#ffffff', bg='#000000', highlightbackground = '#000000',highlightcolor= '#000000',highlightthickness=2,bd =1)

label_F_h_m = tk.Label(window, text = 'dlugosc jumpera antenowego [m]: ', font=('Arial',10),fg='#ffffff',bg='#000000')
dlugosc_jumpera_antenowego_var = Spinbox(window, from_=1, to=8888888888888888888,font=('Arial',10),fg='#ffffff', bg='#000000', highlightbackground = '#000000',highlightcolor= '#000000',highlightthickness=2,bd =1)

label_Gb = tk.Label(window, text = 'zysk energetyczny anteny stacji bazowej [dBi]: ', font=('Arial',10),fg='#ffffff',bg='#000000')
Gb_var = Spinbox(window, from_=1, to=8888888888888888888,font=('Arial',10),fg='#ffffff', bg='#000000', highlightbackground = '#000000',highlightcolor= '#000000',highlightthickness=2,bd =1)

label_return = tk.Label(window, text = '', font=('Arial',10),fg='#ffffff',bg='#000000')

sub_btn=tk.Button(window,text = 'Przelicz', command = fun.dlugosc_skuteczna_anteny_polfalowej,fg='#ffffff', bg='#000000', highlightbackground = '#000000',highlightcolor= '#000000',highlightthickness=2,bd =1)

label_f.grid(row=1,column=0)
f_var.grid(row=1,column=1)

label_dmax.grid(row=2,column=0)
dmax_var.grid(row=2,column=1)

label_A.grid(row=3,column=0)
A_var .grid(row=3,column=1)

label_h1.grid(row=4,column=0)
h1_var.grid(row=4,column=1)

label_s_w.grid(row=5,column=0)
s_w_var.grid(row=5,column=1)

label_c_m.grid(row=6,column=0)
c_m_var.grid(row=6,column=1)

label_h2.grid(row=7,column=0)
h2_var.grid(row=7,column=1)

label_elementy.grid(row=8,column=1)

label_Pn.grid(row=9,column=0)
Pn_var.grid(row=9,column=1)

label_alfa.grid(row=10,column=0)
alfa_fidera_antenowego_var.grid(row=10,column=1)

label_F_elementu.grid(row=11,column=0)
F_dlugosc_fidera_antenowego_var.grid(row=11,column=1)

label_alfa_jumpera.grid(row=12,column=0)
alfa_jumpera_antenowego_var.grid(row=12,column=1)

label_F_h_m.grid(row=13,column=0)
dlugosc_jumpera_antenowego_var.grid(row=13,column=1)

label_Gb.grid(row=14,column=0)
Gb_var.grid(row=14,column=1)

sub_btn.grid(row=15,column=1)
label_return.grid(row=16,column=0,columnspan=3)





window.mainloop()

