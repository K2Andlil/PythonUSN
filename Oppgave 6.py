# Oppgave 6

import numpy as np
import matplotlib.pyplot as plt


def f(x):
    return -x**2-5

liste_x = np.linspace(-10, 10, 200)
liste_y = f(liste_x)

plt.plot(liste_x,liste_y)
print(plt.show())

