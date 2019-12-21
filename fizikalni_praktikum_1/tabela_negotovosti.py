# made with heart by Gregor Zunic

from sympy import *
import math
import numpy as np
import matplotlib.pyplot as plt
from decimal import Decimal

'''
izracun nagotovsti v enacbah

treba je installat:

pip install sympy, numpy, matplotlib

kt v Projekt Tomo se spreminja samo stvari k so med ##   ##
'''

####################################################################
####################################################################

# to je samo vizualno da se vid kaj se za rezultat dubi
racunamo = 'k'

# vazn samo za koncn output, za velikost texta
text_size = 20

# za vsak simbol k se ga uporab v enacbi (function) je treba narest symbol (lahko je z latex formatingom, samo more bit r'')
ro, d1, d2 = symbols(r'\rho d_1 d_2')

# za vsako neznanko nrdimo tuple, (x, []) prvi el v listu je velikost neznanke, drugi el je napaka
data = [
    (ro, [13000, 0]),
    (d1, [0.006, 0.1*10**-6]),
    (d2, [0.0128, 0.1*10**-6])
]

# tuki se definira funkcijo, lahko se uporabla use funkcije eg. sin(), ln() iz numpy-ja in sympy-ja
function = ro*(1/(pi*d2**2)**2-1/(pi*d1**2)**2)/2

####################################################################
####################################################################

# ne spreminjat, mislm lah ampak se lah kej breaka

values = [(x[0], x[1][0]) for x in data]

results = []

for el in data:
    deriv = Derivative(function, el[0])
    res = deriv.doit()
    deltaa = el[1][1]
    error = (float(deriv.doit().subs(values) * deltaa))
    latfunc = '$'+latex(res)+'$'
    results.append((latfunc, deltaa, '%.4E' % Decimal(error)))

final_error = sqrt(sum([abs(float(x[2])**2) for x in results]))
print(final_error)

if not text_size:
    text_size = 15

columns = [r'$\frac{\partial %s}{\partial x_i}$' % racunamo,
           r'$\sigma_i$', r'$\sigma_i \cdot \frac{\partial %s}{\partial x_i}$' % racunamo]
rows = ['$'+str(x[0])+'$' for x in data]

plt.title('Negotovost za funkcijo')

plt.xticks([])
plt.yticks([])

plt.subplots_adjust(left=0.05, bottom=0, right=0.97, top=0.94)

plt.axis('off')

table = plt.table(cellText=results, loc='center left',
                  rowLabels=rows, colLabels=columns)

plt.text(0.35, 0.85, '$'+racunamo+'=' +
         latex(function)+'$', fontsize=text_size+5)
table.set_fontsize(text_size)
table.scale(1, 4)
table.auto_set_font_size(False)

plt.text(0.35, 0.1, r'$\Delta '+racunamo+' = ' +
         '%.4E' % final_error+'$', fontsize=text_size+4)


plt.show()
