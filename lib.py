
import math
import webbrowser

from test import T_Pola

class Antena:
    def dlugosc_skuteczna_anteny_polfalowej(self,czestotliwosc):
        Lambda_m = int(3e8) / int( czestotliwosc )
        return Lambda_m / math.pi
    
    
    def obl_chronionej_war_nat_P_Elektrycznego(self,cz_mocowa_odb,Zwej,wsp_ochronny,dlugosc_skuteczna_anteny_polfalowej):
        Pomin = math.pow(10,int(cz_mocowa_odb))/10
        Eomin = 3.16e4*math.sqrt(Pomin*Zwej)
        Emin_czul = 20*math.log(((2*Eomin)/dlugosc_skuteczna_anteny_polfalowej)/1)
        return Emin_czul + int(wsp_ochronny)
        
    def Dobor_elementow(self):
        webbrowser.open('https://www.rfsworld.com/#') # Dobor parametrow
            
    def Zastepcza_Moc_Promieniowa(self,Moc_Nadajnika,tlumienie_fidera_Ant,dlugosc_fidera_Ant,Zysk_E_Ant_S_Bazowej):
        tlumienie_podstawowe_fidera = 0.01 * int(tlumienie_fidera_Ant) * int(dlugosc_fidera_Ant)
        return int(Moc_Nadajnika) - tlumienie_podstawowe_fidera + int(Zysk_E_Ant_S_Bazowej) - 2.15 # zwraca w DBW
    
    
    # Pod funkcja do wart nat pola ele na granicy. 
    def T_Pola(E_inf,E_sup,helper,helper2):
        
        E_inf /= 38*10+50 # natezenie pola elektrycznego odczytane z wykresow ITU-R w GIMP [db(uV/m)]
        E_sup /= 38*10+50 # natezenie pola elektrycznego odczytane z wykresow ITU-R w GIMP [db(uV/m)]
        
        E_h1 = E_inf + (E_sup - E_inf) * helper
        return  E_h1 + helper2

    def Wartosc_nat_pola_elektrycznego_na_granicy_zasiegu(self,czestotliwosc,E_inf_min_db_uV_m,E_sup_min_db_uV_m,h1,h2,h_nominalne_ponizej,h_nominalne_powyzej,Z_Moc_promieniowa,H_srodowiska,E_inf_max_db_uV_m,E_sup_max_db_uV_m,f_min_Hz,f_max_Hz):
        k_h2 = 3.2+6.2*math.log(czestotliwosc/10e6)
        
        helper = ((math.log(h1/h_nominalne_ponizej))/(math.log(h_nominalne_powyzej/h_nominalne_ponizej)))
        helper2 = (Z_Moc_promieniowa - 30 ) + k_h2 * math.log(h2/H_srodowiska)
        
        E_h2_min_db_uV_m = T_Pola(E_inf_min_db_uV_m,E_sup_min_db_uV_m,helper,helper2)
        E_h2_max_db_uV_m = T_Pola(E_inf_max_db_uV_m,E_sup_max_db_uV_m,helper,helper2)
        # Z tego mozna zrobic jedna osobna funkcje i po prostu wyliczac 
        return E_h2_min_db_uV_m + (E_h2_max_db_uV_m - E_h2_min_db_uV_m) * ((math.log(czestotliwosc / f_min_Hz)) / (math.log(f_max_Hz / f_min_Hz)))
        