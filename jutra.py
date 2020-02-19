import numpy as np
import math
import matplotlib.pyplot as plt

KOT_META = 65.0  # STOPINJE
V0 = 67.056  # izstopna hitrost puscice iz loka (long bow) m/s
HITROST_VETRA = np.linspace(0, 100, 2)  # hitrost vetra od 0 do 200 m/s
KOEFICIENT_UPORA = 0.2  # lahka puscica / subsonic
RO_ZRAKA = 997  # KG/M₃
POVRSINA_PUSCICE = 0.0008  # M₂
POVRSINA_PUSCICE_CELE = 0.002  # M₂
dT = 10e-3  # tisocinko sekune za dt
MASA = 0.32
VISINA_LOKOSTRELCA = 1.7  # M

KOT_META = (KOT_META / 360) * 2 * 3.141
y_mod = 1



dosegi = {}
#print("kot meta v radijanih je {}".format(KOT_META))
for hitros_vetra in HITROST_VETRA:
    XI = []
    YI = []
    visina = VISINA_LOKOSTRELCA
    pozicija = 0
    x_hitrost = np.cos(KOT_META)*V0
    y_hitrost = np.sin(KOT_META)*V0
    T = 0
    i = 0
    while (visina > 0):
        if i % 100 == 0:
            print(i)
           

        XI.append(pozicija)
        YI.append(visina)
        visina += y_hitrost * dT 
        pozicija += x_hitrost * dT

        v2_y = np.long(y_hitrost)**2.0
        drag_y = np.long(KOEFICIENT_UPORA * RO_ZRAKA * v2_y * (POVRSINA_PUSCICE + POVRSINA_PUSCICE_CELE * np.sin(np.tan(y_hitrost/x_hitrost))))
        y_hitrost -= (9.81 * dT) + ((drag_y  / (2.0 * MASA) )* dT * np.abs(y_hitrost)/y_hitrost) * y_mod

        v2_x = (np.long(hitros_vetra + x_hitrost))**2.0
        drag_x = np.long(KOEFICIENT_UPORA * RO_ZRAKA * v2_x * (POVRSINA_PUSCICE + POVRSINA_PUSCICE_CELE * np.cos(np.tan(y_hitrost/x_hitrost))))
        x_hitrost -= (drag_x  / (2.0 * MASA) )* dT
        #print(KOEFICIENT_PORA * RO_ZRAKA * (x_hitrost + hitros_vetra)**2 * POVRSINA_PUSCICE / (2 * MASA) * dT)
        #print(drag, x_hitrost)

        T+= dT
        i += 1

    dosegi[hitros_vetra]=(XI, YI)

for k in dosegi.keys():
    plt.plot(dosegi[k][0], dosegi[k][1], label = "{} [km/h]".format(k*3.6))

#print(dosegi)
plt.legend()
plt.show()


