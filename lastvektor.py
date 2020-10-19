import numpy as np

def lastvektor(nelem, last, moment, fastinnspeningsmoment):
    #Lastvektoren inneholder to bidrag
    #1)Konsentrerte knutepunktskrefter og momenter i knutepunktene
    #2)Knutepunktskrefter og momenter som skyldes last i felt
    
    #Lager en array der man kan legge inn lastene
    #nelem er lengden på arrayet
    #tallet en er hvor mange delemententer hvert element betsår av
    lastvektor = np.zeros(nelem, 1)
    
    
    #Legger inn momenter som skyldes krefter i felt, 
    #dvs fastinnspeningsmoment
    
    for i in fastinnspeningsmoment:
        
    #Legger til ytre krefter som vikrer i knutepunktene
    #Det er kun en av lastene som bidrar til dette
    #og det er momentet i element nr 7
    
    for a in last:
        if a[0]==4: #sjekker om lasten er et moment
        
            knutepunktmoment=a[7] #finner knutetpunktet momente virker i
            lastvektro[knutepunktmoment-1] += a[7]
            
    return lastvektor
        
            
    
    
