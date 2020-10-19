import numpy as np


def endeM ( nelem , elem , elementlengder , rot , fim , boyestivheter ):
    endemom = np . zeros (( nelem , 2) ) # Oppretter tomt array for aa lagre
    # endemomentene i.
    r = np . zeros (( nelem , 2) ) # Oppretter tomt array for aa lagre rotasjoner brukt
    # i mellomregning i.
    k = np . array ([[4 , 2] , [2 , 4]]) # Oppretter en generell lokal stivhetsmatrise .
    for i in range ( nelem ) :
        eilk = k *( boyestivheter [i ]/ elementlengder [i ]) # Ganger EI/L inn i den
    # lokale stivhetsmatrisen .
        r[i ][0] = rot [ elem [ i ][0] -1] # Lagrer rotasjonen i lokal ende 1 til
    # elementet i arrayet "r".
        r[i ][1] = rot [ elem [ i ][1] -1] # Lagrer rotasjonen i lokal ende 2 til
    # elementet i arrayet "r".
        endemom [i] = eilk.dot (r[ i ]) # Ganger den lokale stivhetsmatrisen med
    # rotasjonene i endene paa elementet og lagrer resultatet i arrayet
    # " endemom ".
        endemom [i ][0] += fim [i][0] # Legger til fastinnspenningsmomentet i
    # lokal ende 1.
        endemom [i ][1] += fim [i][1] # Legger til fastinnspenningsmomentet i
    # lokal ende
    return endemom
