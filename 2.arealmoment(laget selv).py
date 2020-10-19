import numpy as np

def arealmoment(ntvsnitt, tvsnitt, nelem, elem):
    andreArealmoment = np.zeros((nelem, 1))
    for i in range(nelem):
        if elem[i][4] == 1: #hvis I-profil
            tvsnitt_I = tvsnitt[0]
            hs = tvsnitt_I[1] #høyde steg
            ts = tvsnitt_I[2] #tykkelse steg 
            tft = tvsnitt_I[3] #tykkelse flens topp
            bft = tvsnitt_I[4] #bredde flens topp
            tfb = tvsnitt_I[5] #tykkelse flens bunn
            bfb = tvsnitt_I[6] #bredde flens bunn
            #bruker steiners teorem til å finne 2. arealmoment for I-profil
            I = 1/12* (hs * ts**3) 
            + 1/12 * tft * bft**3 + tft * bft * 0.5 * (hs + tft)
            + 1/12 * tfb * bfb**3 +  tfb * bfb * 0.5 * (hs + tfb)
            andreArealmoment[i] = I
           
        elif elem[i][4] == 2: #hvis rør
            tvsnitt_r = tvsnitt[1]
            d = tvsnitt_r[0] #diameter
            t = tvsnitt_r[1] #tykkelse
            #finner 2.arealmoment for rørtverrsnitt
            I = np.pi/64 * (d**4 - (d-2*t)**4) # pi/64 * (Dy^4 - Di^4)
        
            andreArealmoment[i] = I

    return andreArealmoment #returnerer 2. arealmoment



