import numpy as np

def boyestivhet(element, nelement, ntvsnitt, tvsnitt):
    
    #lager en tom array for å lagre data for boyestivhet
    boyestivhet = np.zeros(nelem, 1)
    
    #lager en tom array for å lagre data for andre Arealmoment
    andreAmom = np.zeros(nelem, 1)

    #lager en tom arrat for å lagre data for aralsenteret
    arealsenter = np.zeros(nelem, 1)
    
    #lager variabler for å kunne beregne boyestivheten
    ttf = btf = tbf = bbf = hs = ts = d = t = 0
    
    #gir verdier til elementene
    for i in range(nelem):
        #finner ut hvilken type yversnitt det er
        tverrsnittsnummer = elem[i][3]
        #egen løkke for om det er kun ett tversnitt
        if ntvsnitt == 1:
            tvsnittype = tvsnitt[1]
            if tvsnittype == 1:#i-profil
                btf = tvsnitt[2] #bunn topp flens
                ttf = tvsnitt[3] #topp topp flens
                bbf = tvsnitt[4] #bunn bunn flens
                tbf = tvsnitt[5] #topp bunn flens
                hs = tvsnitt[6] #hoyde steg
                bs = tvsnitt[7] #bunn steg
            elif tvsnittype == 2: #rør
                d = tvsnitt[2] #diameter rør
                t = tvsnitt[3] #tykkelse rør
        else:
            # tar minus en pga inderksreing i python
            tvsnittype = tvsnitt[tversnittnummer-1][1]
            if tvsnitttype == 1:
                #samme som i oppgaven over
                btf = tvsnitt[tversnittnummer-1][2]
                ttf = tvsnitt[tversnittnummer-1][3]
                bbf = tvsnitt[tversnittnummer-1][4]
                tbf = tvsnitt[tversnittnummer-1][5]
                hs = tvsnitt[tversnittnummer-1][6]
                bs = tvsnitt[tversnittnummer-1][7]
            elif tvsnittype == 2:
                d = tvsnitt[tversnittnummer-1][2]
                t = tvsnitt[tversnittnummer-1][3]
                
        if ntvsnittype == 1:   
            #bergener arealsenter
            zc = ((bbf*tbf*(tbf/2))+((hs-ttf-tbf)*ts*(hs/2)+btf)+(btf*ttf*(hs-(ttf/2))))\
            /((bbf*tbf)+((hs-ttf)*ts)+(btf*tft))
            
            #bergener andre arealmoment
            I = (1/12)*bbf*tbf**3+bbf*tbf*(zc-(tbf/2))**2+\
                (1/12)*ts*(hs-ttf-tbf)**3 + ts*(hs-ttf-tbf)*(abs((hs/2)-zc))**2 +\
                (1/12)*btf*ttf**3 + btf*ttf*(hs-zc-(ttf/2))**2
                
            #legger til verdier i de tomme arrayene
            boyestivhet[i] = I
            andreAmom[i] = I 
            arealsenter[i] = zc
            
        elif ntvsnittype == 2:
            #bergener arealsente
            zc = d/2
            
            #bergener andre arealmoment
            I = (np.pi*(((d/2)**4)-((d/2)-t)**4))/4
            
            boyestivhet[i] = I
            andreAmom[i] = I 
            arealsenter[i] = zc
        
        #berregner boyestiheten
        boyestivhet[i] *= elem[i][2]
        
        return boyestivhet, andreAmom, arealsenter
            
            
            
            
            