import math


def T_Pola(E_inf,E_sup,helper,helper2):
        
        E_inf /= 38*10+50 # natezenie pola elektrycznego odczytane z wykresow ITU-R w GIMP [db(uV/m)]
        E_sup /= 38*10+50 # natezenie pola elektrycznego odczytane z wykresow ITU-R w GIMP [db(uV/m)]
        
        E_h1 = E_inf + (E_sup - E_inf) * helper
        return  E_h1 + helper2
    
def Wartosc_nat_pola_elektrycznego_na_granicy_zasiegu(czestotliwosc,E_inf_min_db_uV_m,E_sup_min_db_uV_m,h1,h2,h_nominalne_ponizej,h_nominalne_powyzej,Z_Moc_promieniowa,H_srodowiska,E_inf_max_db_uV_m,E_sup_max_db_uV_m,f_min_Hz,f_max_Hz):
        k_h2 = 3.2+6.2*math.log(czestotliwosc/10e6)
        
        helper = ((math.log(h1/h_nominalne_ponizej))/(math.log(h_nominalne_powyzej/h_nominalne_ponizej)))
        helper2 = (Z_Moc_promieniowa - 30 ) + k_h2 * math.log(h2/H_srodowiska)
        
        E_h2_min_db_uV_m = T_Pola(E_inf_min_db_uV_m,E_sup_min_db_uV_m,helper,helper2)
        E_h2_max_db_uV_m = T_Pola(E_inf_max_db_uV_m,E_sup_max_db_uV_m,helper,helper2)
        # Z tego mozna zrobic jedna osobna funkcje i po prostu wyliczac 
        return E_h2_min_db_uV_m + (E_h2_max_db_uV_m - E_h2_min_db_uV_m) * ((math.log(czestotliwosc / f_min_Hz)) / (math.log(f_max_Hz / f_min_Hz)))
    
    
czestotliwosc = 1
E_inf_min_db_uV_m = 1 
E_sup_min_db_uV_m = 1
h1 = 1
h2 = 1 
h_nominalne_ponizej = 1
h_nominalne_powyzej = 1
Z_Moc_promieniowa = 1
H_srodowiska = 1 
E_inf_max_db_uV_m = 1
E_sup_max_db_uV_m = 1
f_min_Hz = 1
f_max_Hz = 1
    
print(Wartosc_nat_pola_elektrycznego_na_granicy_zasiegu(czestotliwosc,E_inf_min_db_uV_m,E_sup_min_db_uV_m,h1,h2,h_nominalne_ponizej,h_nominalne_powyzej,Z_Moc_promieniowa,H_srodowiska,E_inf_max_db_uV_m,E_sup_max_db_uV_m,f_min_Hz,f_max_Hz))