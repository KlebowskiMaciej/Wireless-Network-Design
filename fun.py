import main
import math


def dlugosc_skuteczna_anteny_polfalowej():
    #impedancja
    Zwej = 50;
    Lambda_m = int(3e8) / int( main.f_var.get() )
     
    #Dlugosc skuteczna anteny terminala
    l_skuteczne = Lambda_m / math.pi
   
    #Obliczenie chronionej wartości natężenia pola elektrycznego
    Pomin = math.pow(10,int(main.c_m_var.get()))/10
    Eomin = 3.16e4*math.sqrt(Pomin*Zwej)
    Emin_czul = 20*math.log(((2*Eomin)/l_skuteczne)/1)
    Emin_chron = Emin_czul + int(main.A_var.get())
    
    #Obliczanie zastepczej mocy promieniowej
    Moc_nadajnika_Watt = math.pow(10,int(main.Pn_var.get())/10)
    tlumienie_podstawowe_fidera = 0.01 * int(main.alfa_fidera_antenowego_var.get()) * int(main.F_dlugosc_fidera_antenowego_var.get())
    tlumienie_dodatkowe = 0.01 * int(main.alfa_jumpera_antenowego_var.get())*int(main.dlugosc_jumpera_antenowego_var.get())
    Zastepcza_moc_promieniowa_dBW = int(main.Pn_var.get()) - tlumienie_podstawowe_fidera + int(main.Gb_var.get()) - 2.15
    Zastepcza_moc_promieniowa_W = math.pow(10,Zastepcza_moc_promieniowa_dBW/10)
    P_eirp_dBi = Zastepcza_moc_promieniowa_dBW + 2.15
    Moc_dostarczana_do_anteny_dBW = int(main.Pn_var.get()) - tlumienie_podstawowe_fidera - tlumienie_dodatkowe
    r_m = 10  # nie mam pojecia co to
    najwiekszy_wymiar_anteny = 10
    S_W_m2 =  Zastepcza_moc_promieniowa_W / (4 * math.pi * r_m * r_m)
    D_m = 1.007 # Najwiekszy wymiar anteny ?
    r_d_m = (2*math.pow(D_m,2))/ Lambda_m
    
    # Obliczenie poprawki na moc
    poprawka_na_moc_dB = int(main.Pn_var.get()) - 30

    
    
    
    return main.label_return.config(text='Dlugosc skuteczna anteny terminala:  '+str(l_skuteczne)+
                                        '\n chroniona wartosc natezenia pola elektrycznego:  '+
                                        str(Emin_chron)+'\n Zastepcza moc proeminiowa:  '+
                                        str(Zastepcza_moc_promieniowa_dBW)+'\n Moc dostarczona do antent  '
                                        +str(Moc_dostarczana_do_anteny_dBW)+ '\n Zastepcza moc promieniowa  '+str(Zastepcza_moc_promieniowa_dBW)+'\n poprawka na moc:  '+ str(poprawka_na_moc_dB))