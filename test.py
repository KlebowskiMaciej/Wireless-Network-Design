import matplotlib.pyplot as plt

def trz_dwa(XLabel,E_min_chron_alfa1,E_min_chron_alfa2,E_min_chron_alfa3,E_min_chron_alfa4,E_min_chron,title):
        
    plt.plot(XLabel, E_min_chron, label = "E min chron")
    plt.plot(XLabel, E_min_chron_alfa1, label = "α=2,492")
    plt.plot(XLabel, E_min_chron_alfa2, label = "α=2,583")
    plt.plot(XLabel, E_min_chron_alfa3, label = "α=2,977")
    plt.plot(XLabel, E_min_chron_alfa4, label = "α=3,235")
    plt.xlabel('PN')
    plt.ylabel('')
    plt.title(title)
    plt.legend()
    plt.show()
       
E_min_chron = [23.074,23.074,23.074,23.074,23.074,23.074,23.074,23.074,23.074,23.074,23.074,23.074,23.074,23.074,23.074,23.074,23.074,23.074,23.074,23.074]
E_min_chron_alfa1 = [15.305728261938,18.3160282185778,20.0769408091346,21.3263281752176,22.2954283052982,23.0872407657744,23.7567086620805,24.3366281318574,24.8481533563312,25.305728261938,25.7196551135202,26.0975407224142,26.4451617850063,26.7670086187203,27.0666408524948,27.3469280884972,27.6102174757207,27.858453312971,28.0932642714663,28.3160282185778]
E_min_chron_alfa2 = [15.305728261938,18.3160282185778,20.0769408091346,21.3263281752176,22.2954283052982,23.0872407657744,23.7567086620805,24.3366281318574,24.8481533563312,25.305728261938,25.7196551135202,26.0975407224142,26.4451617850063,26.7670086187203,27.0666408524948,27.3469280884972,27.6102174757207,27.858453312971,28.0932642714663,28.3160282185778]
E_min_chron_alfa3 = [15.305728261938,18.3160282185778,20.0769408091346,21.3263281752176,22.2954283052982,23.0872407657744,23.7567086620805,24.3366281318574,24.8481533563312,25.305728261938,25.7196551135202,26.0975407224142,26.4451617850063,26.7670086187203,27.0666408524948,27.3469280884972,27.6102174757207,27.858453312971,28.0932642714663,28.3160282185778]
E_min_chron_alfa4 = [15.305728261938,18.3160282185778,20.0769408091346,21.3263281752176,22.2954283052982,23.0872407657744,23.7567086620805,24.3366281318574,24.8481533563312,25.305728261938,25.7196551135202,26.0975407224142,26.4451617850063,26.7670086187203,27.0666408524948,27.3469280884972,27.6102174757207,27.858453312971,28.0932642714663,28.3160282185778]
PN = [0.5,1,1.5,2,2.5,3,3.5,4,4.5,5,5.5,6,6.5,7,7.5,8,8.5,9,9.5,10]
trz_dwa(PN,E_min_chron_alfa1,E_min_chron_alfa2,E_min_chron_alfa3,E_min_chron_alfa4,E_min_chron,"3.2.1")
        
        
        
        
        
        





