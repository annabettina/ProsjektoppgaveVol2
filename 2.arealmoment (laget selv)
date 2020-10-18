import numpy as np

def arealmoment(ntvsnitt, tvsnitt):
    for i in range(ntvsnitt):
        if tvsnitt[i] == 1: #hvis I-profil
            hs = tvsnitt[i][1] #høyde steg
            ts = tvsnitt[i][2] #tykkelse steg 
            tft = tvsnitt[i][3] #tykkelse flens topp
            bft = tvsnitt[i][4] #bredde flens topp
            tfb = tvsnitt[i][5] #tykkelse flens bunn
            bfb = tvsnitt[i][6] #bredde flens bunn
            #bruker steiners teorem til å finne 2. arealmoment for I-profil
            I = 1/12* (hs * ts**3) + 
                1/12 * tft * bft**3 + tft * bft * 0.5 * (hs + tft) + 
                1/12 * tfb * bfb**3 +  tfb * bfb * 0.5 * (hs + tfb)
        elif tvsnitt[i] == 2: #hvis rør
            d = tvsnitt[i][0] #diameter
            t = tvsnitt[i][1] #tykkelse
            #finner 2.arealmoment for rørtverrsnitt
            I = np.pi/64 * (d**4 - (d-2*t)**4) # pi/64 * (Dy^4 - Di^4)

    return I #returnerer 2. arealmoment


