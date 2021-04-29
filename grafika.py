# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 18:03:57 2021

@author: nerea
"""

import matplotlib.pyplot as plt
import numpy as np


#Gasaren dentsitatea
def dent_gas(r):
    return 1700*(r**-1.5)

#Hautsaren dentsitatea
def dent_hauts(r):
    return np.where(r < 2.7, dent_gas(r)/240, dent_gas(r)/60)
 

#Diskoaren tenperatura
def tenp(r):
    return 280*(r**-0.5)

#Planetak kokatzeko grafikan
letra = ['Merkurio', 'Artizarra', 'Lurra', 'Marte', 'Jupiter', 'Saturno',
         'Urano', 'Neptuno']
dist_plan = np.array([0.39, 0.723, 1, 1.524, 5.203, 9.539, 19.18, 30.06])

#Materiaren kondentsazioa
r_kon = 2.7


#Grafikako datuak kalkulatu
r = np.linspace(0.35, 36, 1000)
tenp_list = tenp(r)
gas_list = dent_gas(r)
hauts_list = dent_hauts(r)
hautsa_plan = dent_hauts(dist_plan)


#----------------GRAFIKAK SORTZEKO-----------------
fig, (ax_den, ax_ten) = plt.subplots(nrows=2, ncols=1, sharex=True)


# Grafikan textua jarri
ax_den.set_title('Gainazal dentsitatea')
ax_den.set_ylabel(r'$\Sigma \; (g\,cm^{-2})$')
ax_den.set_yscale('log')
ax_den.legend()

ax_ten.set_title('Tenperatura')
ax_ten.set_xlabel('r (AU)')
ax_ten.set_ylabel('T (K)')
ax_ten.set_xscale('log')
ax_ten.set_yscale('log')

# Grafikatu
ax_den.plot(r, gas_list, label='Gasa')
ax_den.plot(r, hauts_list, label='Hautsa')
ax_den.scatter(dist_plan, hautsa_plan)

# Planetetan izenak jarri
for i, letra in enumerate(letra):
    ax_den.annotate(letra, (dist_plan[i], hautsa_plan[i]), (1.1*dist_plan[i],
                    hautsa_plan[i]), size=7)

# Materia kondentsatuko deneko distantzia adierazteko
t = np.linspace(np.amin(tenp_list), np.amax(tenp_list), 100)
sigma = np.linspace(np.amin(hauts_list), np.amax(gas_list), 100)
ax_ten.plot(np.full(100, r_kon), t, linestyle='--', color='grey')
ax_ten.scatter(r_kon, tenp(r_kon))
ax_ten.annotate('170 K', (r_kon, tenp(r_kon)), (1.1*r_kon, tenp(r_kon)))
ax_den.plot(np.full(100, r_kon), sigma, linestyle='--', color='grey')
ax_ten.plot(r, tenp_list)

plt.show()
