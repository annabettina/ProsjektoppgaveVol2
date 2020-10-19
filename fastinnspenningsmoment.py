import numpy as np

def fastmomenter(npunkt, elem, nelem, nlast, last, elementlengde):
    
    fastinnspenningsmoment = np.zeros((nelem, 2))

    for i in range(nlast): #går gjennom lastene
        L = elementlengde[i] #finner elementlengde
        elemnr = int(last[i][1]) #henter ut elementnr
        
        if last[i][0] == 1: #hvis punktlast
            alpha = last[i][3]
            a = alpha * L #avstand fra ende 1
            b = L - a #avstand fra ende 2
            P = last[i][2] #henter ut lastverdien
            if last[i][4] == 0: #sjekker at lasten står vinkelrett på elementet
                #hentet fra kompendiet tabell 8.3
                fastinnspenningsmoment[elemnr-1][0] += (-P * a * b**2) / L**2 #moment ende 1
                fastinnspenningsmoment[elemnr-1][1] += (P * a**2 * b) / L**2 #moment ende 2
            else: #hvis ikke vinkelrett på element
                P = (last[i][2])/(np.cos(last[i][4]*np.pi/180)) #finner komponent vinkelrett på element
                #hentet fra kompendiet tabell 8.3
                fastinnspenningsmoment[elemnr-1][0] += (-P * a * b**2) / L**2 #moment ende 1
                fastinnspenningsmoment[elemnr-1][1] += (P * a**2 *b) / L**2 #moment ende 2

        elif last[i][0] == 2: #hvis jevnt fordelt last (rektangel)
                q = last[i][5] #henter ut lastverdi for jevn fordelt last
                #hentet fra kompendiet tabell 8.3
                fastinnspenningsmoment[elemnr-1][0] += (-q * L**2)/12 #moment ende 1
                fastinnspenningsmoment[elemnr-1][1] += (q * L**2)/12 #moment ende 2
        elif last[i][0] == 3: #hvis lineært fordelt last (trekant)
            q1 = last[i][5] #verdi q1
            q2 = last[i][6] #verdi q2

            if q1 < q2: #hvis last ende 1 mindre enn last ende 2
                #hentet fra kompendiet tabell 8.3
                fastinnspenningsmoment[elemnr-1][0] += (-q2 * L**2) / 30 #moment ende 1
                fastinnspenningsmoment[elemnr-1][1] += (q2 * L**2) / 20 #moment ende 2
            else:
                #hentet fra kompendiet tabell 8.3
                fastinnspenningsmoment[elemnr-1][0] += (-q1 * L**2) / 20 #moment ende 1
                fastinnspenningsmoment[elemnr-1][1] += (q1 * L**2) / 30 #moment ende 2

    return fastinnspenningsmoment


