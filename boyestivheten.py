import numpy as np

def boyestivhet(element, nelement, ntvsnitt, tvsnitt):
    #dette er kokt, så nav og noen ting må endres
    boyestivhet = np.zeros(nelem, 1)
    
    andreAmom = np.zeros(nelem, 1)

    arealsenter = np.zeros(nelem, 1)
    
    btf = ttf = bbf = tbf = hs = ts = d = t = 0
    
    for i in range(nelem):
        tverrsnittsnummer = elem[i][3]
        if ntvsnitt == 1:
            tvsnittype = tvsnitt[1]
            if tvsnittype == 1:
                btf = tvsnitt[2]
                ttf = tvsnitt[3]
                bbf = tvsnitt[4]
                tbf = tvsnitt[5]
                hs = tvsnitt[6]
                bs = tvsnitt[7]
            elif tvsnittype == 2:
                d = tvsnitt[2]
                t = tvsnitt[3]
        else:
            tvsnittype = tvsnitt[tversnittnummer-1][1]
            if tvsnitttype == 1:
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
            zc = ((bbf*tbf*(tbf/2))+((hs-ttf-tbf)*ts*(hs/2)+btf)+(btf*ttf*(hs-(ttf/2))))\
            /((bbf*tbf)+((hs-ttf)*ts)+(btf*tft))
            
            I = (1/12)*bbf*tbf**3+bbf*tbf*(zc-(tbf/2))**2+\
                (1/12)*ts*(hs-ttf-tbf)**3 + ts*(hs-ttf-tbf)*(abs((hs/2)-zc))**2 +\
                (1/12)*btf*ttf**3 + btf*ttf*(hs-zc-(ttf/2))**2
                
            boyestivhet[i] = I
            andreAmom[i] = I 
            arealsenter[i] = zc
            
        elif ntvsnittype == 2:
            zc = d/2
            
            I = (np.pi*(((d/2)**4)-((d/2)-t)**4))/4
            
            boyestivhet[i] = I
            andreAmom[i] = I 
            arealsenter[i] = zc
            
        boyestivhet[i] *= elem[i][2]
        return boyestivhet, andreAmom, arealsenter
            
            
            
            
            