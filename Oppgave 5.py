# Oppgave 5

import numpy as np
import math as math

a = float(input("Skriv inn diameteren på sirkelen i figuren i cm: "))
b = float(input("Skriv inn lengden på trekanten i figuren i cm: "))
r = (a/2)
A_halvsirkel = (np.pi*r**2)/2
O_halvsirkel = (2*np.pi*r)/2
Areal_trekant = (b*a)/2
c2 = (a**2)+(b**2)
O_trekant = math.sqrt(c2) + a + b

Areal = A_halvsirkel + Areal_trekant
Omkrets = O_halvsirkel + O_trekant

Areal_avrundet = round(Areal, 2)
Omkrets_avrundet = round(Omkrets, 2)

print(f"Arealen av figuren er: {Areal_avrundet} cm\nOmkretsen av figuren er {Omkrets_avrundet} cm")
