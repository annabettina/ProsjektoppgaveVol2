import numpy as np

def lastvektor ( npunkt , nelem , elem , fim , nlast , last ):
   
    lastvektor = np.zeros ((npunkt , 1))
    for i in range (nelem):
        knpkt1 = elem[i][0]
        knpkt2 = elem[i][1]
        lastvektor[knpkt1-1] -= fim[i][0]
        lastvektor[knpkt2-1] -= fim[i][1] 

        for j in range (nlast):
            knpunktLast = int(last[j][7])
            lastvektor[knpunktLast-1] += last[j][8]

    return lastvektor
