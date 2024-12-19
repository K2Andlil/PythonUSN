# Oppgave 3

import numpy as np

v_grad = float(input('Skriv inn gradtallet: '))
v_rad = (v_grad*np.pi/180)
v_rad_avrundet = round(v_rad, 2)
print(f'Radiantallet til vinkelel er {v_rad_avrundet}.')