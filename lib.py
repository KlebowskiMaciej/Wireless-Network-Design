from fun import dlugosc_skuteczna_anteny_polfalowej
import math
import webbrowser

class Antena:
    def dlugosc_skuteczna_anteny_polfalowej(self,czestotliwosc):
        Lambda_m = int(3e8) / int( czestotliwosc )
        return Lambda_m / math.pi
    
    
    def obl_chronionej_war_nat_P_Elektrycznego(self,cz_mocowa_odb,Zwej,czestotliwosc,wsp_ochronny):
        Pomin = math.pow(10,int(cz_mocowa_odb))/10
        Eomin = 3.16e4*math.sqrt(Pomin*Zwej)
        Emin_czul = 20*math.log(((2*Eomin)/dlugosc_skuteczna_anteny_polfalowej(self,czestotliwosc))/1)
        return Emin_czul + int(wsp_ochronny)
        
    def Dobor_elementow(self):
        webbrowser.open('http://google.com') # Dobor parametrow
            
    def Zastepcza_Moc_Promieniowa(self,Moc_Nadajnika,tlumienie_fidera_Ant,dlugosc_fidera_Ant,Zysk_E_Ant_S_Bazowej):
        tlumienie_podstawowe_fidera = 0.01 * int(tlumienie_fidera_Ant) * int(dlugosc_fidera_Ant)
        return int(Moc_Nadajnika) - tlumienie_podstawowe_fidera + int(Zysk_E_Ant_S_Bazowej) - 2.15 # zwraca w DBW

        