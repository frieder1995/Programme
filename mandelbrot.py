# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import matplotlib.pyplot as plt


x_val = np.arange(-2,2,0.001)
y_val = np.copy(x_val)*1j
dimx = len(x_val)
dimy = len(y_val)
schärfe = 50
bildpunkte = np.zeros((dimx,dimy))

for i in range(dimx):
    for j in range(dimy):
        z = 0 + 0j
        for n in range(schärfe):
            if abs(z) > 2:
                bildpunkte[j][i] = n/schärfe
                break
            z = z*z + x_val[i]+y_val[j]

bildpunkte[bildpunkte == 0] = 1
plt.imshow(bildpunkte)
plt.show()

            
